# coding=utf-8

from myfaker.provider.StatusProvider import StatusProvider
from tables.base_table import TableBase


class Vehicle(TableBase):
    """
    整车数据格式和定义
    车辆状态
    充电状态
    运行模式
    车速
    累计里程
    总电压
    总电流
    SOC
    DC-DC状态
    档位
    绝缘电阻
    预留
    """
    def __init__(self):
        self.table_name = "Vehicle"

        self.vehicle_status = StatusProvider(1, 3)
        self.charge_status = StatusProvider(1, 4)
        self.mode_status = StatusProvider(1, 3)
        self.speed = StatusProvider(0, 2200, len_byte=2)
        self.mileage = StatusProvider(0, 999999, len_byte=4)  # 取值范围是0~9999999，但是太大这里先去99999
        self.voltage = StatusProvider(0, 10000, len_byte=2)
        self.current_flows = StatusProvider(0, 20000, len_byte=2)
        self.soc = StatusProvider(0, 100)
        self.dc_dc = StatusProvider(1, 2)
        self.gears = StatusProvider(0, 63, error_status=False)  # 存疑问，档位是否覆盖0~15
        self.resistance = StatusProvider(0, 60000, error_status=False)
        self.reserve = StatusProvider(0, 0, error_status=False)

        self.add_col(self.vehicle_status)
        self.add_col(self.charge_status)
        self.add_col(self.mode_status)
        self.add_col(self.speed)
        self.add_col(self.mileage)
        self.add_col(self.voltage)
        self.add_col(self.current_flows)
        self.add_col(self.soc)
        self.add_col(self.dc_dc)
        self.add_col(self.gears)
        self.add_col(self.resistance)
        self.add_col(self.reserve)


if __name__ == "__main__":
    # Vehicle().gen_lines(200)
    import time
    start = float(time.time()) * 1000
    v = Vehicle()
    print("Total Time token: %d ms" % (time.time() * 1000 - start))
    for _ in range(0, 2000):
        v.gen_one_row()
    take_time = float(time.time() * 1000 - start)
    print("Total Time token: %d ms" % take_time)
