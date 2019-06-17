# coding=utf-8

from myfaker.provider.StatusProvider import StatusProvider
from tables.base_table import TableBase


class Extremum(TableBase):
    def __init__(self):
        self.table_name = "Extremum"

        self.highest_battery_sys_index = StatusProvider(1, 250)
        self.highest_battery_single_index = StatusProvider(1, 250)
        self.highest_battery_vol = StatusProvider(0, 15000, len_byte=2)
        self.lowest_battery_sys_index = StatusProvider(1, 250)
        self.lowest_battery_single_index = StatusProvider(1, 250)
        self.lowest_battery_vol = StatusProvider(0, 15000, len_byte=2)
        self.highest_temperature_sys = StatusProvider(1, 250)
        self.highest_temperature_single = StatusProvider(1, 250)
        self.highest_temperature = StatusProvider(0, 250)
        self.lowest_temperature_sys = StatusProvider(1, 250)
        self.lowest_temperature_single = StatusProvider(1, 250)
        self.lowest_temperature = StatusProvider(0, 250)

        self.add_col(self.highest_battery_sys_index)
        self.add_col(self.highest_battery_single_index)
        self.add_col(self.highest_battery_vol)
        self.add_col(self.lowest_battery_sys_index)
        self.add_col(self.lowest_battery_single_index)
        self.add_col(self.lowest_battery_vol)
        self.add_col(self.highest_temperature_sys)
        self.add_col(self.highest_temperature_single)
        self.add_col(self.highest_temperature)
        self.add_col(self.lowest_temperature_sys)
        self.add_col(self.lowest_temperature_single)
        self.add_col(self.lowest_temperature)


if __name__ == "__main__":
    Extremum().gen_lines(200)
