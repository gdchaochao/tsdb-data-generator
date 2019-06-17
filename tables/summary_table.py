# coding=utf-8

import time
import os
import csv
from tables.base_table import TableBase
from tables.vehicle import Vehicle
from tables.motors import Motors
from tables.motor import Motor
from tables.battery import Battery
from tables.engine import Engine
from tables.location import Location
from tables.extremum import Extremum
from tables.alter import Alter
from myfaker.provider.VINProvider import VINProvider


class Summary(TableBase):
    def __init__(self):
        self.table_name = "Summary"

        start = float(time.time()) * 1000

        Vehicle()
        end_time = float(time.time() * 1000)
        print("Init time token: %d" % (end_time - start))
        start = end_time

        Motors()
        end_time = float(time.time() * 1000)
        print("Init time token: %d" % (end_time - start))
        start = end_time

        Motor()
        end_time = float(time.time() * 1000)
        print("Init time token: %d" % (end_time - start))
        start = end_time

        Battery()
        end_time = float(time.time() * 1000)
        print("Init time token: %d" % (end_time - start))
        start = end_time

        Engine()
        end_time = float(time.time() * 1000)
        print("Init time token: %d" % (end_time - start))
        start = end_time

        Location()
        end_time = float(time.time() * 1000)
        print("Init time token: %d" % (end_time - start))
        start = end_time

        Extremum()
        end_time = float(time.time() * 1000)
        print("Init time token: %d" % (end_time - start))
        start = end_time

        Alter()
        end_time = float(time.time() * 1000)
        print("Init time token: %d" % (end_time - start))

        self.vin = VINProvider()

    def write_faker_by_sec(self, lines, output_path="./data/"):
        start = float(time.time()) * 1000
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        try:
            r_path = output_path + self.table_name + ".csv"
            if os.path.exists(r_path):
                os.remove(r_path)
            f = open(r_path, 'a', newline='')
            csv_write = csv.writer(f, dialect='excel')
            car_index = 0
            title_row = ["timestamp", "tag(VIN)"]
            for _ in range(1, 61):
                title_row.append("value " + str(_))
            csv_write.writerow(title_row)
            for _ in range(0, lines):
                t = int(round(time.time() * 1000))
                row = self.gen_one_row()
                row[0] = t
                row[1] = self.vin.random_status()
                csv_write.writerow(row)
                car_index = car_index + 1
        except IOError:
            print("IO Error.")
        finally:
            f.close()
        take_time = float(time.time() * 1000 - start)
        print("Gen Time token: %d ms" % take_time)


if __name__ == "__main__":
    Summary().gen_lines(200)
