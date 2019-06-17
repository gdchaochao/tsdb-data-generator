# coding=utf-8

from myfaker.provider.StatusProvider import StatusProvider
from tables.base_table import TableBase


class Motor(TableBase):
    def __init__(self):
        self.table_name = "Motor"

        self.motor_id = StatusProvider(1, 253, error_status=False)
        self.motor_status = StatusProvider(1, 4)
        self.ctl_temperature = StatusProvider(0, 250)
        self.speed = StatusProvider(0, 65531, len_byte=2)
        self.torque = StatusProvider(0, 65531, len_byte=2)
        self.motor_temperature = StatusProvider(0, 250)
        self.ctl_input_voltage = StatusProvider(0, 60000, len_byte=2)
        self.ctl_electric_current = StatusProvider(0, 20000, len_byte=2)

        self.add_col(self.motor_id)
        self.add_col(self.motor_status)
        self.add_col(self.ctl_temperature)
        self.add_col(self.speed)
        self.add_col(self.torque)
        self.add_col(self.motor_temperature)
        self.add_col(self.ctl_input_voltage)
        self.add_col(self.ctl_electric_current)


if __name__ == "__main__":
    Motor().gen_lines(200)
