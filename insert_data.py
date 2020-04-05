
import sqlite3

__all__ = [
    '_insert_records'
]


class InsertData(object):
    insert_table_command = "INSERT INTO"

    def __init__(self, table_name, data: dict, ):
        self.table_name = table_name
        self.data = data
        self.insert_table_command += f" {self.table_name}"

    def parse_insert_columns(self):
        insert_cols = ", ".join([k for k in self.data])
        table_cols = " (" + insert_cols + ")"
        self.insert_table_command += table_cols

    # def parse_insert_rows(self):
    #     insert_records = ", ".join([str(v) for _, v in self.data.items()])
    #     insert_records = " values (" + insert_records + ")"
    #     self.insert_table_command += insert_records

    def parse_insert_q_marks(self):
        q_marks = ", ".join(["?" for _ in self.data])
        q_marks = " values (" + q_marks + ")"
        self.insert_table_command += q_marks

    def create_insert_record_command(self):
        self.parse_insert_columns()
        self.parse_insert_q_marks()
        return self.insert_table_command


def _insert_records(table_name, con: sqlite3.connect, data):
    for d in data:
        cls = InsertData(table_name, d)
        cmd = cls.create_insert_record_command()
        cur = con.cursor()
        records = tuple(str(val) for _, val in d.items())
        cur.execute(cmd, records)
        con.commit()
        cur.close()
