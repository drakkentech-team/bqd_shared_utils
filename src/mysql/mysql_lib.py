import mysql.connector as c

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
             post: str = "", get_columns: bool = False, debug: bool = False, where_values: Tuple = ()) \
        -> Tuple[List[List], List]:
    """
    retreive data from columns in table, filtered by a where statement
    """

    db = connect(*db_connect)
    if where:
        where = where.replace(" = 'None'", " is null")
    sql = f"{pre}SELECT {columns} FROM {table} {join if join else ''} { where if where else ''} " \
          f"{order if order else ''}{post}"

    if debug:
        print(f"\nSQL is \n{sql} \n with where values {where_values}")

    my_cursor = db.cursor(prepared=True)
    my_cursor.execute(sql, where_values)
    data = my_cursor.fetchall()
    field_names = [i[0] for i in my_cursor.description] if get_columns else None
    return data, field_names


def get_flat_column_data(table: str, column: str, where: str = None, where_values: Tuple = ()):
    """
    get data from column in table and flatten it
    """

    data = get_data(table, column, where=where, where_values=where_values)[0]
    return list(chain(*data))


def make_where(records_to_match: Union[List[Dict], Dict]) -> Tuple[str, Tuple]:
    """
    make a prepared where statement to match to either to a list of records or to a single record
    """

    if type(records_to_match) == dict:
        return make_single_where(records_to_match)
    elif type(records_to_match) == list and len(records_to_match):
        return make_multi_where(records_to_match)


def make_single_where(record: Dict) -> Tuple[str, Tuple]:
    statements, values = [], []
    for k, v in record.items():
        if v is None:
            statement = f"{k} is null"
        else:
            statement = f"{k} = %s"
            values.append(v)
        statements.append(statement)
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
