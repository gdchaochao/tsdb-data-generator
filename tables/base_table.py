# coding=utf-8

import os
import time
import csv


class TableBase(object):
    column_list = []
    spilt = "|"
    table_name = "table"

    def add_col(self, status):
        self.column_list.append(status)

    def add_cols(self, status_list):
        self.column_list.extend(status_list)

    def get_column(self):
        return self.column_list

    def gen_one_line(self):
        line = ""
        for col in self.column_list:
            line = line + str(col.random_status()) + self.spilt
        return line

    def set_table_name(self, name):
        self.table_name = name

    def gen_one_row(self):
        row = []
        for col in self.column_list:
            row.append(col.random_status())
        return row

    def gen_lines(self, lines, output_path="./data/"):
        print("genera data, table " + self.table_name)
        start = time.time()
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        try:
            f = open(output_path + self.table_name + ".csv", 'a', newline='')
            csv_write = csv.writer(f, dialect='excel')
            for _ in range(0, lines):
                csv_write.writerow(self.gen_one_row())
        except IOError:
            print("IO Error.")
        finally:
            f.close()
        end = time.time()
        print("Time token: %d s" % (end - start))






