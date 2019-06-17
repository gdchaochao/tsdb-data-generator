# coding=utf-8

from myfaker.provider.StatusProvider import StatusProvider
from tables.base_table import TableBase


class Engine(TableBase):
    def __init__(self):
        self.table_name = "Engine"

        self.engine_status = StatusProvider(1, 2)
        self.engine_speed = StatusProvider(0, 60000, len_byte=2)
        self.engine_effectiveness = StatusProvider(0, 60000, len_byte=2)

        self.add_col(self.engine_status)
        self.add_col(self.engine_speed)
        self.add_col(self.engine_effectiveness)


if __name__ == "__main__":
    Engine().gen_lines(200)
