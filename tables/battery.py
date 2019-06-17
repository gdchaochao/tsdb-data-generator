# coding=utf-8

from myfaker.provider.StatusProvider import StatusProvider
from tables.base_table import TableBase


class Battery(TableBase):
    def __init__(self):
        self.table_name = "Battery"

        self.battery_vol = StatusProvider(0, 20000, len_byte=2)
        self.battery_current = StatusProvider(0, 20000, len_byte=2)
        self.battery_fuel_rate = StatusProvider(0, 60000, len_byte=2)
        self.battery_temperature_probes = StatusProvider(0, 65531, len_byte=2)
        self.battery_temperature = StatusProvider(0, 240, error_status=False)  # 不定长，暂时只支持一个
        self.highest_temperature = StatusProvider(0, 2400, len_byte=2)
        self.highest_tem_probes = StatusProvider(1, 252)
        self.most_concentration = StatusProvider(0, 60000, len_byte=2)
        self.most_concentration_index = StatusProvider(1, 252)
        self.most_pressure = StatusProvider(0, 1000, error_status=False, len_byte=2)
        self.most_pressure_index = StatusProvider(1, 252)
        self.battery_dc_dc = StatusProvider(1, 2)

        self.add_col(self.battery_vol)
        self.add_col(self.battery_current)
        self.add_col(self.battery_fuel_rate)
        self.add_col(self.battery_temperature_probes)
        self.add_col(self.battery_temperature)
        self.add_col(self.highest_temperature)
        self.add_col(self.highest_tem_probes)
        self.add_col(self.most_concentration)
        self.add_col(self.most_concentration_index)
        self.add_col(self.most_pressure)
        self.add_col(self.most_pressure_index)
        self.add_col(self.battery_dc_dc)


if __name__ == "__main__":
    Battery().gen_lines(200)
