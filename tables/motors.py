# coding=utf-8

from myfaker.provider.StatusProvider import StatusProvider
from tables.base_table import TableBase


class Motors(TableBase):
    def __init__(self):
        self.table_name = "Motors"

        self.motor_number = StatusProvider(1, 253, error_status=False)
        self.motor_msg = StatusProvider(1, 0xffff, len_byte=4, error_status=False)

        self.add_col(self.motor_number)
        self.add_col(self.motor_msg)


if __name__ == "__main__":
    Motors().gen_lines(200)
