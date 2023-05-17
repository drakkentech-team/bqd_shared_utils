from pickle import NONE
import mysql.connector as c
import logging
from bqd_shared_utils.src.general.logging import log
from mysql.connector.errors import OperationalError, InterfaceError
from _mysql_connector import MySQLInterfaceError
from time import sleep


try:
    from config import db_connect
except ImportError:
    from connect.settings import db_connect


from typing import Tuple, List, Union, Dict
from itertools import chain


def connect(host, user, password, database, port):
    """
    connect to a my_sql database
    """

    target_db = c.connect(host=host, user=user, password=password, database=database, port=port,
                          auth_plugin='mysql_native_password')
    return target_db


def get_data(table: str, columns: str, join: str = None, where: str = None, order: str = None, pre: str = "",
             post: str = "", get_columns: bool = False, debug: bool = False, where_values: Tuple = (),
             flatten_columns: bool = False, db_override: tuple = None) -> Tuple[List[List], List]:
    try:
        return _get_data(table, columns, join, where, order, pre, post, get_columns, debug, where_values,
                         flatten_columns, db_override)
    except (OperationalError, InterfaceError) as e:
        print(f'Got some error! {e}')
        sleep(30)
        return _get_data(table, columns, join, where, order, pre, post, get_columns, debug, where_values,
                         flatten_columns, db_override)


def _get_data(table: str, columns: str, join: str = None, where: str = None, order: str = None, pre: str = "",
             post: str = "", get_columns: bool = False, debug: bool = False, where_values: Tuple = (),
             flatten_columns: bool = False, db_override: tuple = None) -> Tuple[List[List], List]:
    """
    retreive data from columns in table, filtered by a where statement
    """

    if not db_override:
        db = connect(*db_connect)
    else:
        db = connect(*db_override)

    if where:
        where = where.replace(" = 'None'", " is null")
    sql = f"{pre}SELECT {columns} FROM {table} {join if join else ''} { where if where else ''} " \
          f"{order if order else ''}{post}"

    if debug:
        print(f"\nSQL is \n{sql} \n with where values {where_values}")

    my_cursor = db.cursor(prepared=True)
    my_cursor.execute(sql, where_values)
    data = my_cursor.fetchall()
    field_names = [i[0] for i in my_cursor.description] if (get_columns and data) else None

    if flatten_columns and data:
        columns = [[] for column in data[0]]
        for record in data:
            for i, value in enumerate(record):
                columns[i].append(value)
        data = columns
    my_cursor.close()
    return data, field_names


def get_flat_column_data(table: str, column: str, where: str = None, where_values: Tuple = ()):
    """
    get data from column in table and flatten it
    """

    data = get_data(table, column, where=where, where_values=where_values)[0]
    return list(chain(*data))


def make_where(records_to_match: Union[List[Dict], Dict], tolerant_strings: bool = False,
               case_insensitive: bool = False, force_case_sensitive: bool = False,
               logger=None) -> Tuple[str, Tuple]:
    """
    make a prepared where statement to match to either to a list of records or to a single record
    """

    if type(records_to_match) == dict:
        return make_single_where(records_to_match, tolerant_strings, case_insensitive, force_case_sensitive, logger)
    elif type(records_to_match) == list and len(records_to_match):
        return make_multi_where(records_to_match)


def make_single_where(record: Dict, tolerant_strings: bool = False, case_insensitive: bool = False,
                      force_case_sensitive: bool = False, logger=None) -> Tuple[str, Tuple]:
    statements, values = [], []
    for k, v in record.items():
        if v is None:
            statement = f"{k} is null"
        elif type(v) == list:
            if len(v) == 0:
                log('WARNING: empty list of values encountered in make_single_where', logger, 'warning')
                continue
            statement, phs = '', []  # placeholders
            for r in v:
                values.append(r)
                phs.append("%s")
            statement = f"{k} in ({', '.join(phs)})"
        elif type(v) == dict:
            inner_statement = []
            for ik, iv in v.items():
                if iv is None:
                    log(f"WARNING: {iv} in {ik} is null", logger, 'warning')
                elif type(iv) == str:
                    if tolerant_strings:
                        values.append('%' + iv + '%')
                        inner_statement.append(f'{ik} LIKE %s')
                    else:
                        values.append(iv)
                        inner_statement.append(f'{ik} = %s')
                else:
                    values.append(iv)
                    inner_statement.append(f'{ik} = %s')
            
            if len(inner_statement) > 0:
                statement = '(' + ' OR '.join(inner_statement) + ')'
        else:
            upper_pre = 'UPPER(' if case_insensitive and type(v) == str else ''
            upper_post = ')' if case_insensitive and type(v) == str else ''
            if tolerant_strings and type(v) == str:
                binary = 'BINARY ' if force_case_sensitive else ''
                statement = f"{upper_pre}{k}{upper_post} like {binary}%s"
                values.append(f"%{v.upper() if case_insensitive else v}%")
            else:
                statement = f"{k} = {upper_pre}%s{upper_post}"
                values.append(v)

        statements.append(statement)
    if len(statements) == 0:
        log('WARNING: tried to make a where but no valid conditions resulted!', logger, 'warning')
        return '', ()

    return "WHERE (" + " AND ".join(statements) + ")", tuple(values)

def make_multi_where(record: List[Dict]) -> Tuple[str, Tuple]:
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
        out = out + q + str((placeholder or e)) + q + ", "
    out = out + q + str((placeholder or list_in[-1])) + q + ")"
    return out


def insert(table_name: str, record: Union[dict, list[dict]], debug: bool = False, return_record: bool = False,
           match_keys: str = None):
    try:
        _insert(table_name, record, debug, return_record, match_keys)
    except (MySQLInterfaceError, OperationalError, InterfaceError) as e:
        print(f'Error! {e}')
        print('but we wont panic, well wait 30s and try again')
        sleep(30)
        _insert(table_name, record, debug, return_record, match_keys)


def _insert(table_name: str, record: Union[dict, list[dict]], debug: bool = False, return_record: bool = False,
           match_keys: str = None):
    """ Inserts new records into a mySql table

    if a list of records are given, many will be inserted, else just one

    Args:
        table_name:
        record:         a dict with keys corresponding to field names in mySql
                        OR a list of such dicts
        debug:

    """
    if not record:
        return

    db = connect(*db_connect)
    my_cursor = db.cursor(prepared=True)

    cols = list(record.keys()) if type(record) == dict else list(record[0].keys())
    sql = f'''INSERT INTO {table_name} {list_to_tuple(cols)} VALUES {list_to_tuple(cols, placeholder='%s')}'''

    if type(record) == dict:
        values = tuple([record[k] for k in cols])
        log_sql(sql, values, debug)
        my_cursor.execute(sql, values)
    else:
        values = [tuple([row[k] for k in cols]) for row in record]
        for v in values:
            log_sql(sql, v, debug)
        my_cursor.executemany(sql, values)

    db.commit()
    my_cursor.close()

    if return_record:
        return get_inserted_records(table_name, record, keys=match_keys, debug=debug)


def get_inserted_records(table_name: str, record: Union[Dict, List[Dict]], keys: List[str] = None,
                         debug: bool = False) -> List[Dict]:
    """ gets the records that was inserted into a mySql table, with any automatic
        and defualt field values that may have been assigned,
        if a list of keys is specified, the match will be based on only the listed keys
    """
    if type(record) == list:
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
    if type(values) == tuple:
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


def make_wheres(record: Dict, keys: List[str] = None) -> Tuple[str, List]:
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


def get_ordered_data(table: str, columns: str, join: str = None, where: str = None, order: str = None,
                     pre: str = "", post: str = "", debug: bool = False, where_values: Tuple = (),
                     db_override: tuple = None) -> List[dict]:
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

    data, field_names = get_data(table, columns, join, where=where, order=order, get_columns=True, pre=pre, post=post,
                                 debug=debug, where_values=where_values, db_override=db_override)
    ordered_data = []
    for line in data:
        record = convert_two_lists_to_dict(field_names, line)
        ordered_data.append(record)
    return ordered_data


def convert_two_lists_to_dict(keys: list, values: list) -> dict:
    """
    makes a dictionary with keys and values
    obviously, keys and values must be in matching order and of matching
    length
    """

    output = {}
    for i, j in zip(keys, values):
        output[i] = j
    return output


def update(table_name: str, record: Union[dict, List[dict]], debug: bool = False, primary_key: str = 'sid'):
    try:
        _update(table_name, record, debug, primary_key)
    except BaseException as e:
        print(f"got error {e} trying to call sql update!")
        sleep(30)
        _update(table_name, record, debug, primary_key)


def _update(table_name: str, record: Union[dict, List[dict]], debug: bool = False, primary_key: str = 'sid'):
    """ Updates records in a mySql table

        if a list of records are given, many will be inserted, else just one
        Note: records must have a key 'sid' with a valid value

        Args:
            table_name:
            record:         a dict with keys corresponding to field names in mySql
                            OR a list of such dicts
            debug:

        """
    if not record:
        return

    db = connect(*db_connect)
    my_cursor = db.cursor(prepared=True)
    if type(record) == dict:
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
    my_cursor.close()


def set_column_value(table_name: str, column_name: str, value, condition: str = 'sid > 0', debug: bool = False):
    db = connect(*db_connect)
    my_cursor = db.cursor(prepared=True)
    sql = f'''UPDATE
    {table_name}
    SET
    {column_name} = %s
    WHERE
    {condition}'''
    my_cursor.execute(sql, (value, ))
    db.commit()
    my_cursor.close()
