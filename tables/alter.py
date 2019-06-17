# coding=utf-8

from myfaker.provider.StatusProvider import StatusProvider
from tables.base_table import TableBase


class Alter(TableBase):
    def __init__(self):
        self.table_name = "Alter"

        self.alter_level = StatusProvider(0, 3)
        self.alter_sign = StatusProvider(0, 0xff, error_status=False, len_byte=4)  # 32位的标志位，这里几个32位数字都简化
        self.battery_fault_num = StatusProvider(0, 252)
        self.battery_fault_list = StatusProvider(0, 0, error_status=False, len_byte=4)  # TODO 这里取值范围太大，暂时为0
        self.motor_fault_num = StatusProvider(0, 252)
        self.motor_fault_list = StatusProvider(0, 0, error_status=False, len_byte=4)
        self.engine_fault_num = StatusProvider(0, 252)
        self.engine_fault_list = StatusProvider(0, 0, error_status=False, len_byte=4)
        self.other_fault_num = StatusProvider(0, 252)
        self.other_fault_list = StatusProvider(0, 0, error_status=False, len_byte=4)

        self.add_col(self.alter_level)
        self.add_col(self.alter_sign)
        self.add_col(self.battery_fault_num)
        self.add_col(self.battery_fault_list)
        self.add_col(self.motor_fault_num)
        self.add_col(self.motor_fault_list)
        self.add_col(self.engine_fault_num)
        self.add_col(self.engine_fault_list)
        self.add_col(self.other_fault_num)
        self.add_col(self.other_fault_list)


if __name__ == "__main__":
    Alter().gen_lines(200)
