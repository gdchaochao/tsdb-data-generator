# coding=utf-8

from faker import Faker
import math


# 状态位Provider
class LocationProvider(object):
    def __init__(self, loc_type):
        """
        产生地理位置的provider
        :param type: 0表示latitude, 1表示longitude
        """
        self.loc_type = loc_type
        self.fake = Faker()

    def random_status(self):
        if self.loc_type == 0:
            return int(math.fabs(self.fake.latitude() * 1000000))
        else:
            return int(math.fabs(self.fake.longitude() * 1000000))


if __name__ == "__main__":
    sp = LocationProvider(1)
    print(sp.random_status())
