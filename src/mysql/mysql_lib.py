import logging
import os
import sys
import traceback
from itertools import chain
from time import sleep
from typing import Any

from mysql.connector import pooling
from mysql.connector.errors import InterfaceError, OperationalError, PoolError

from bqd_shared_utils.src.general.logging import log

try:
    from config import db_connect
except ImportError:
    import importlib

    db_connect = importlib.import_module("connect.settings").db_connect

POOL_SIZE = int(os.getenv("MYSQL_POOL_SIZE", "20"))
POOL_NAME = os.getenv("MYSQL_POOL_NAME", "ithemba_mysql_lib_pool")
_db_pool: pooling.MySQLConnectionPool | None = None
RET_BACKOFF_SECONDS = float(os.getenv("MYSQL_RETRY_BACKOFF_SECONDS", "0.5"))
ERROR_MISSING_DB_SETTINGS = "Missing database connection settings."
ERROR_WHERE_VALUES_MISSING = "Parameterized WHERE clause supplied without corresponding where_values."
ERROR_WHERE_VALUES_INSUFFICIENT = "Insufficient where_values supplied for parameterized WHERE clause."
ERROR_RAW_WHERE_DISABLED = (
    "Raw WHERE clause usage is disabled by SQL_ENFORCE_WHERE_PARAMS; please provide placeholders and where_values."
)
ERROR_SUSPICIOUS_WHERE = "Suspicious token detected in WHERE clause; refusing to execute raw SQL."
ERROR_WHERE_UNMATCHED_SINGLE = "WHERE clause contains unmatched single quotes; aborting execution."
ERROR_WHERE_UNMATCHED_DOUBLE = "WHERE clause contains unmatched double quotes; aborting execution."


def _get_pool(
    host: str | None,
    user: str | None,
    password: str | None,
    database: str | None,
    port: int | str | None,
) -> pooling.MySQLConnectionPool:
    global _db_pool
    if _db_pool is None:
        if host is None or user is None or password is None or database is None or port is None:
            raise ValueError(ERROR_MISSING_DB_SETTINGS)
        _db_pool = pooling.MySQLConnectionPool(
            pool_name=POOL_NAME,
            pool_size=POOL_SIZE,
            pool_reset_session=True,
            host=host,
            user=user,
            password=password,
            database=database,
            port=port,
            auth_plugin="mysql_native_password",
        )
        logging.info("Initialized MySQL Connection Pool")
    return _db_pool


def connect(
    host: str | None,
    user: str | None,
    password: str | None,
    database: str | None,
    port: int | str | None,
) -> Any:
    """
    Get a connection from the pool, initializing it if necessary.
    """
    try:
        pool = _get_pool(host, user, password, database, port)
    except Exception:
        logging.exception("Failed to initialize connection pool")
        raise
    try:
        return pool.get_connection()
    except PoolError:
        logging.exception("Connection pool exhausted")
        raise


STRICT_WHERE_PARAMS = os.getenv("SQL_ENFORCE_WHERE_PARAMS", "false").lower() in {"1", "true", "yes"}


def _validate_where_clause(where: str | None, where_values: tuple | list | None):
    """Basic guard rails for WHERE clauses before executing prepared statements."""

    if not where:
        return

    placeholder_count = where.count("%s")

    if placeholder_count:
        if not where_values:
            raise ValueError(ERROR_WHERE_VALUES_MISSING)

        if len(where_values) < placeholder_count:
            raise ValueError(ERROR_WHERE_VALUES_INSUFFICIENT)

    elif STRICT_WHERE_PARAMS:
        raise ValueError(ERROR_RAW_WHERE_DISABLED)

    suspicious_tokens = ("{", "}", "--", "/*", "*/", ";")
    if any(tok in where for tok in suspicious_tokens):
        raise ValueError(ERROR_SUSPICIOUS_WHERE)

    if where.count("'") % 2 == 1:
        raise ValueError(ERROR_WHERE_UNMATCHED_SINGLE)

    if where.count('"') % 2 == 1:
        raise ValueError(ERROR_WHERE_UNMATCHED_DOUBLE)


def get_data(
    table: str,
    columns: str,
    join: str | None = None,
    where: str | None = None,
    order: str | None = None,
    pre: str = "",
    post: str = "",
    get_columns: bool = False,
    debug: bool = False,
    where_values: tuple = (),
    flatten_columns: bool = False,
    db_override: tuple | None = None,
    limit: int | None = None,
    offset: int | None = None,
) -> tuple[list, list | None]:
    try:
        return _get_data(
            table,
            columns,
            join,
            where,
            order,
            pre,
            post,
            get_columns,
            debug,
            where_values,
            flatten_columns,
            db_override,
            limit,
            offset,
        )
    except (OperationalError, InterfaceError, PoolError) as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        tb_str = "\n".join(traceback.format_tb(exc_traceback))
        detail = f"Exception Type: {exc_type}\nException Value: {exc_value}\nTraceback: {tb_str}"
        print(f"Got some error! {e}\n{detail}")
        sleep(5)  # Reduced sleep time
        return _get_data(
            table,
            columns,
            join,
            where,
            order,
            pre,
            post,
            get_columns,
            debug,
            where_values,
            flatten_columns,
            db_override,
            limit,
            offset,
        )


def _get_data(
    table: str,
    columns: str,
    join: str | None = None,
    where: str | None = None,
    order: str | None = None,
    pre: str = "",
    post: str = "",
    get_columns: bool = False,
    debug: bool = False,
    where_values: tuple = (),
    flatten_columns: bool = False,
    db_override: tuple | None = None,
    limit: int | None = None,
    offset: int | None = None,
) -> tuple[list, list | None]:
    """
    retreive data from columns in table, filtered by a where statement
    """
    db = None
    my_cursor = None
    try:
        db = connect(*db_connect) if not db_override else connect(*db_override)

        if where:
            _validate_where_clause(where, where_values)
            where = where.replace(" = 'None'", " is null")

        sql = (
            f"{pre} SELECT {columns} FROM {table}"
            f" {join if join else ''}"
            f" {where if where else ''}"
            f" {order if order else ''}"
            f" {f'LIMIT {limit}' if limit else ''}"
            f" {f'OFFSET {offset}' if offset else ''}"
            f"{post}"
        )

        if debug:
            print(f"\nSQL is \n{sql} \n with where values {where_values}")

        my_cursor = db.cursor(prepared=True)
        my_cursor.execute(sql, where_values)
        data = my_cursor.fetchall()
        field_names = [i[0] for i in my_cursor.description] if (get_columns and data) else None

        if flatten_columns and data:
            flattened_columns = [[] for _ in data[0]]
            for record in data:
                for i, value in enumerate(record):
                    flattened_columns[i].append(value)
            data = flattened_columns
    except BaseException as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        tb_str = "\n".join(traceback.format_tb(exc_traceback))
        detail = f"Exception Type: {exc_type}\nException Value: {exc_value}\nTraceback: {tb_str}"
        print(f"Got some error! {e}\n{detail}")
        raise
    else:
        return data, field_names
    finally:
        if my_cursor:
            my_cursor.close()
        if db:
            db.close()


def execute_statement(sql_statement: str, placeholder_vals: tuple, connection, commit=True, fetch=False):
    my_cursor = None
    try:
        my_cursor = connection.cursor(prepared=True)
        my_cursor.execute(sql_statement, placeholder_vals)

        data = []
        if commit:
            connection.commit()
        if fetch:
            data = my_cursor.fetchall()
    except BaseException as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        tb_str = "\n".join(traceback.format_tb(exc_traceback))
        detail = f"Exception Type: {exc_type}\nException Value: {exc_value}\nTraceback: {tb_str}"
        print(f"Got some error! {e}\n{detail}")
        raise
    else:
        return data
    finally:
        if my_cursor:
            my_cursor.close()


def get_flat_column_data(table: str, column: str, where: str | None = None, where_values: tuple = ()):
    """
    get data from column in table and flatten it
    """

    data = get_data(table, column, where=where, where_values=where_values)[0]
    return list(chain(*data))


def make_where(
    records_to_match: list[dict] | dict,
    tolerant_strings: bool = False,
    case_insensitive: bool = False,
    force_case_sensitive: bool = False,
    logger=None,
) -> tuple[str, tuple]:
    """
    make a prepared where statement to match to either to a list of records or to a single record
    """

    if isinstance(records_to_match, dict):
        return make_single_where(records_to_match, tolerant_strings, case_insensitive, force_case_sensitive, logger)
    if isinstance(records_to_match, list) and len(records_to_match):
        return make_multi_where(records_to_match)
    return "", ()


def make_single_where(
    record: dict,
    tolerant_strings: bool = False,
    case_insensitive: bool = False,
    force_case_sensitive: bool = False,
    logger=None,
) -> tuple[str, tuple]:
    statements, values = [], []
    for k, v in record.items():
        statement = None
        if v is None:
            statement = f"{k} is null"
        elif isinstance(v, list):
            if len(v) == 0:
                log("WARNING: empty list of values encountered in make_single_where", logger, "warning")
                continue
            statement, phs = "", []  # placeholders
            for r in v:
                values.append(r)
                phs.append("%s")
            statement = f"{k} in ({', '.join(phs)})"
        elif isinstance(v, dict):
            inner_statement = []
            for ik, iv in v.items():
                if iv is None:
                    log(f"WARNING: {iv} in {ik} is null", logger, "warning")
                elif isinstance(iv, str):
                    if tolerant_strings:
                        values.append("%" + iv + "%")
                        inner_statement.append(f"{ik} LIKE %s")
                    else:
                        values.append(iv)
                        inner_statement.append(f"{ik} = %s")
                else:
                    values.append(iv)
                    inner_statement.append(f"{ik} = %s")

            if len(inner_statement) > 0:
                statement = "(" + " OR ".join(inner_statement) + ")"
        else:
            upper_pre = "UPPER(" if case_insensitive and isinstance(v, str) else ""
            upper_post = ")" if case_insensitive and isinstance(v, str) else ""
            if tolerant_strings and isinstance(v, str):
                binary = "BINARY " if force_case_sensitive else ""
                statement = f"{upper_pre}{k}{upper_post} like {binary}%s"
                values.append(f"%{v.upper() if case_insensitive else v}%")
            else:
                statement = f"{k} = {upper_pre}%s{upper_post}"
                values.append(v)

        if statement:
            statements.append(statement)
    if len(statements) == 0:
        log("WARNING: tried to make a where but no valid conditions resulted!", logger, "warning")
        return "", ()

    return "WHERE (" + " AND ".join(statements) + ")", tuple(values)


def make_multi_where(record: list[dict]) -> tuple[str, tuple]:
    keys = record[0].keys()
    wheres = []
    where_values = []
    for k in keys:
        phs = []  # placeholders
        for r in record:
            where_values.append(r[k])
            phs.append("%s")
        wheres.append(f"{k} in ({', '.join(phs)})")
    where = f"WHERE ({' AND '.join(wheres)})"
    return where, tuple(where_values)


def list_to_tuple(list_in: list, placeholder=None, add_quotes=False):
    out = "("
    if not list_in:
        return "()"
    q = "'" if add_quotes else ""

    for e in list_in[:-1]:
        out = out + q + str(placeholder or e) + q + ", "
    out = out + q + str(placeholder or list_in[-1]) + q + ")"
    return out


def insert(
    table_name: str,
    record: dict | list[dict],
    debug: bool = False,
    return_record: bool = False,
    match_keys: list[str] | None = None,
):
    try:
        _insert(table_name, record, debug, return_record, match_keys)
    except (OperationalError, InterfaceError) as e:
        print(f"Error! {e}")
        print("but we wont panic, well wait 30s and try again")
        sleep(5)
        _insert(table_name, record, debug, return_record, match_keys)


def _insert(
    table_name: str,
    record: dict | list[dict],
    debug: bool = False,
    return_record: bool = False,
    match_keys: list[str] | None = None,
):
    """Inserts new records into a mySql table

    if a list of records are given, many will be inserted, else just one

    Args:
        table_name:
        record:         a dict with keys corresponding to field names in mySql
                        OR a list of such dicts
        debug:

    """
    db = None
    my_cursor = None
    try:
        if not record:
            return

        db = connect(*db_connect)
        my_cursor = db.cursor(prepared=True)

        cols = list(record.keys()) if isinstance(record, dict) else list(record[0].keys())
        sql = f"""INSERT INTO {table_name} {list_to_tuple(cols)} VALUES {list_to_tuple(cols, placeholder="%s")}"""

        if isinstance(record, dict):
            values = tuple([record[k] for k in cols])
            log_sql(sql, values, debug)
            my_cursor.execute(sql, values)
        else:
            values = [tuple([row[k] for k in cols]) for row in record]
            for v in values:
                log_sql(sql, v, debug)
            my_cursor.executemany(sql, values)

        db.commit()

        if return_record:
            return get_inserted_records(table_name, record, keys=match_keys, debug=debug)
    except BaseException as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        tb_str = "\n".join(traceback.format_tb(exc_traceback))
        detail = f"Exception Type: {exc_type}\nException Value: {exc_value}\nTraceback: {tb_str}"
        print(f"Got some error! {e}\n{detail}")
        raise
    finally:
        if my_cursor:
            my_cursor.close()
        if db:
            db.close()


def get_inserted_records(
    table_name: str, record: dict | list[dict], keys: list[str] | None = None, debug: bool = False
) -> list[dict]:
    """gets the records that was inserted into a mySql table, with any automatic
    and defualt field values that may have been assigned,
    if a list of keys is specified, the match will be based on only the listed keys
    """
    if isinstance(record, list):
        statements, values = [], []
        for i in record:
            add_statements, add_values = make_wheres(i, keys)
            statements.append(add_statements)
            values += values + add_values
        where = "WHERE " + " OR ".join(statements)
        where_values = tuple(values)

    else:
        where, where_values = make_wheres(record, keys)
        where = f"WHERE {where}"

    data = get_ordered_data(table_name, "*", where=where, where_values=tuple(where_values), debug=debug)
    return data


def log_sql(statement, values, debug):
    i, msg = 0, statement
    if isinstance(values, tuple):
        while msg.find("%s") != -1:
            msg = msg.replace("%s", str(values[i]), 1)
            i += 1
    elif values is None:
        msg = statement
    else:
        msgs = []
        for r in values:
            s, i = statement, 0
            while s.find("%s") != -1:
                s = s.replace("%s", str(r[i]), 1)
                i += 1
            msgs.append(s)
        msg = "\n".join(msgs)
    if debug:
        logging.info(f"SQL is \n\t\t{msg}\n")


def make_wheres(record: dict, keys: list[str] | None = None) -> tuple[str, list]:
    """
    make a prepared sql WHERE statement to match given record exactly
    if a list of keys is provided, the where will be based on only the listed keys
    """
    statements, values = [], []
    for k, v in record.items():
        if keys and k not in keys:
            continue
        if v is None:
            statement = f"{k} is null"
        else:
            statement = f"{k} = %s"
            values.append(v)
        statements.append(statement)
    return "(" + " AND ".join(statements) + ")", values


def get_ordered_data(
    table: str,
    columns: str,
    join: str | None = None,
    where: str | None = None,
    order: str | None = None,
    pre: str = "",
    post: str = "",
    debug: bool = False,
    where_values: tuple = (),
    db_override: tuple | None = None,
    limit: int | None = None,
    offset: int | None = None,
) -> list[dict]:
    """
    makes a list of objects (as is used in javascript) out of that which is drawn out of sql

    args:
        table: str      the sql table where the data comes from
        columns: str    a string listing the columns wanted, e.g. "name, ref" or "*"
        join:           a join statement
        where: str      a where statement, such as "WHERE sid = 5", can also be ""
        order: str      a ORDER statement, such as "ORDER by sid"
        where_values:   the values that should be substituted into the where

    kwargs:
        debug: bool     do you want to print some feedback?

    returns:
        ordered_data: list[dict]    a list with dictionaries where each row in the sql table
                                    is a dictionary, the sql columns are its keys, and the
                                    values in the sql table are the keys' values
    """

    data, field_names = get_data(
        table,
        columns,
        join,
        where=where,
        order=order,
        get_columns=True,
        pre=pre,
        post=post,
        debug=debug,
        where_values=where_values,
        db_override=db_override,
        limit=limit,
        offset=offset,
    )
    if field_names is None:
        return []
    field_name_list = list(field_names)
    ordered_data = []
    for line in data:
        record = convert_two_lists_to_dict(field_name_list, line)
        ordered_data.append(record)
    return ordered_data


def convert_two_lists_to_dict(keys: list, values: list) -> dict:
    """
    makes a dictionary with keys and values
    obviously, keys and values must be in matching order and of matching
    length
    """

    output = {}
    for i, j in zip(keys, values, strict=False):
        output[i] = j
    return output


def update(table_name: str, record: dict | list[dict], debug: bool = False, primary_key: str = "sid"):
    try:
        _update(table_name, record, debug, primary_key)
    except BaseException as e:
        print(f"got error {e} trying to call sql update!")
        sleep(5)
        _update(table_name, record, debug, primary_key)


def _update(table_name: str, record: dict | list[dict], debug: bool = False, primary_key: str = "sid"):
    """Updates records in a mySql table

    if a list of records are given, many will be inserted, else just one
    Note: records must have a key 'sid' with a valid value

    Args:
        table_name:
        record:         a dict with keys corresponding to field names in mySql
                        OR a list of such dicts
        debug:

    """
    db = None
    my_cursor = None
    try:
        if not record:
            return

        db = connect(*db_connect)
        my_cursor = db.cursor(prepared=True)
        if isinstance(record, dict):
            updates = ", ".join([str(col) + " = %s " for col, val in record.items()])
            where_values = [val for col, val in record.items()]
            sql = f"UPDATE {table_name} SET {updates} WHERE {primary_key} = %s"
            where_values.append(record.get(primary_key))
            log_sql(sql, tuple(where_values), debug)
            my_cursor.execute(sql, tuple(where_values))

        else:
            updates = ", ".join([str(col) + " = %s " for col, val in record[0].items()])
            sql = f"UPDATE {table_name} SET {updates} WHERE {primary_key} = %s"
            values = []
            for r in record:
                where_values = [val for col, val in r.items()]
                where_values.append(r.get(primary_key))
                values.append(tuple(where_values))
            log_sql(sql, values, debug)
            my_cursor.executemany(sql, values)
        db.commit()
    except BaseException as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        tb_str = "\n".join(traceback.format_tb(exc_traceback))
        detail = f"Exception Type: {exc_type}\nException Value: {exc_value}\nTraceback: {tb_str}"
        print(f"Got some error! {e}\n{detail}")
        raise
    finally:
        if my_cursor:
            my_cursor.close()
        if db:
            db.close()


def set_column_value(table_name: str, column_name: str, value, condition: str = "sid > 0"):
    db = None
    my_cursor = None
    try:
        db = connect(*db_connect)
        my_cursor = db.cursor(prepared=True)
        sql = f"""UPDATE
        {table_name}
        SET
        {column_name} = %s
        WHERE
        {condition}"""
        my_cursor.execute(sql, (value,))
        db.commit()
    except BaseException as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        tb_str = "\n".join(traceback.format_tb(exc_traceback))
        detail = f"Exception Type: {exc_type}\nException Value: {exc_value}\nTraceback: {tb_str}"
        print(f"Got some error! {e}\n{detail}")
        raise
    finally:
        if my_cursor:
            my_cursor.close()
        if db:
            db.close()


def delete_record_by_id(table_name: str, id_value, id_column: str = "sid", debug: bool = False):
    try:
        _delete_record_by_id(table_name, id_value, id_column, debug)
    except (OperationalError, InterfaceError) as e:
        print(f"Error! {e}")
        print("but we wont panic, well wait 30s and try again")
        sleep(5)
        _delete_record_by_id(table_name, id_value, id_column, debug)


def _delete_record_by_id(table_name: str, id_value, id_column: str = "sid", debug: bool = False):
    """
    Deletes a record from a table based on the provided ID value

    Args:
        table_name: str      the name of the table from which to delete the record
        id_value:           the value of the ID column for the record to be deleted
        id_column: str      the name of the ID column (default is 'sid')
        debug: bool         indicates whether to print debug information
    """
    db = None
    my_cursor = None
    try:
        db = connect(*db_connect)
        my_cursor = db.cursor(prepared=True)
        sql = f"DELETE FROM {table_name} WHERE {id_column} = %s"
        log_sql(sql, (id_value,), debug)
        my_cursor.execute(sql, (id_value,))
        db.commit()
    except BaseException as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        tb_str = "\n".join(traceback.format_tb(exc_traceback))
        detail = f"Exception Type: {exc_type}\nException Value: {exc_value}\nTraceback: {tb_str}"
        print(f"Got some error! {e}\n{detail}")
        raise
    finally:
        if my_cursor:
            my_cursor.close()
        if db:
            db.close()


def get_table_count(table_name: str, debug: bool = False) -> int:
    """
    Retrieves the count of rows in a table in the MySQL database.

    Args:
        table_name: str     the name of the table to retrieve the count from
        debug: bool         indicates whether to print debug information

    Returns:
        count: int          the count of rows in the specified table
    """
    db = None
    my_cursor = None
    try:
        db = connect(*db_connect)
        my_cursor = db.cursor()
        sql = f"SELECT COUNT(*) FROM {table_name}"
        if debug:
            print(f"SQL Query: {sql}")

        my_cursor.execute(sql)
        count = my_cursor.fetchone()[0]
        if debug:
            print(f"Count of rows in {table_name}: {count}")
    except (OperationalError, InterfaceError) as e:
        print(f"Error! {e}")
        print("but we wont panic, well wait 30s and try again")
        sleep(5)
        return get_table_count(table_name, debug)
    else:
        return count
    finally:
        if my_cursor:
            my_cursor.close()
        if db:
            db.close()
