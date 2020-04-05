
import os
from os.path import join
import json
import sqlite3

import pandas as pd
from connections import get_recently_introduced_bills
from create_table import create_table_command
from insert_data import _insert_records

_parent_path = os.path.dirname(__file__)


def update_table_columns_file():
    res = get_recently_introduced_bills().json()
    data = res['results'][0]['bills']

    df = pd.DataFrame(data)
    datatypes = df.dtypes
    dict_datatypes = datatypes.astype('str').to_dict()
    filename = 'table_columns.json'

    with open(join(_parent_path, filename), 'w') as jfile:
        write_data = json.dumps(dict_datatypes, indent=4)
        jfile.write(write_data)


def insert_records(table_name, conn):
    res = get_recently_introduced_bills().json()
    data = res['results'][0]['bills']
    _insert_records(table_name, conn, data)


if __name__ == "__main__":
    conn = sqlite3.connect('congress_api.db')
    insert_records('congress_bills', conn)
    pass
