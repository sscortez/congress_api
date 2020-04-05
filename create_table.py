
from helpers import load_json

__all__ = [
    'create_table_command'
]


class CreateTable(object):
    create_table_command = "CREATE TABLE"

    def __init__(self, table_name, columns, first_column_primary_key=True):
        self.table_name = table_name
        self.columns = columns
        self.col1_pkey = first_column_primary_key

    def parse_to_create_table_command(self):
        table_cols = ""

        for i, _key in enumerate(self.columns):
            if i == 0:
                data_type = self.columns[_key]
                table_cols += f"{_key} {data_type}"
                if self.col1_pkey is True:
                    table_cols += " PRIMARY KEY"
            else:
                data_type = self.columns[_key]
                table_cols += f", {_key} {data_type}"
        text = " ".join([self.create_table_command, self.table_name, "(" + table_cols + ")"])
        return text


def create_table_command(json_file='table_columns.json', table_name='congress_bills'):
    col_data = load_json(json_file)
    ct = CreateTable(table_name, col_data)
    return ct.parse_to_create_table_command()
