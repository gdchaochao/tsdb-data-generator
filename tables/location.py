# coding=utf-8

from myfaker.provider.StatusProvider import StatusProvider
from myfaker.provider.LocationProvider import LocationProvider
from tables.base_table import TableBase


class Location(TableBase):
    def __init__(self):
        self.table_name = "Location"

        self.location_status = StatusProvider(0, 7, error_status=False)
        # TODO 经度与纬度这里有疑问，60进制的数字乘以10^6？
        self.location_longitude = LocationProvider(1)
        self.location_latitude = LocationProvider(0)

        self.add_col(self.location_status)
        self.add_col(self.location_longitude)
        self.add_col(self.location_latitude)


if __name__ == "__main__":
    Location().gen_lines(200)
