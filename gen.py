#!/usr/bin/python
# coding=utf-8

import sys
import getopt
import time
from tables.summary_table import Summary


def main(argv):
    lines = ''
    output = ''
    try:
        opts, args = getopt.getopt(argv, "hl:o:", ["lines=", "output="])
    except getopt.GetoptError:
        print('gen.py -l <lines_to_gen> -o <output_path>')
        sys.exit(2)
    if len(opts) == 0:
        print('gen.py -l <lines_to_gen> -o <output_path>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('gen.py -l <lines_to_gen> -o <output_path>')
            sys.exit()
        elif opt in ("-l", "--lines"):
            lines = arg
        elif opt in ("-o", "--output"):
            output = arg
    print('Lines to gen：', lines)
    print('Output path：', output)

    s = Summary()
    s.write_faker_by_sec(lines=int(lines), output_path=output)


if __name__ == "__main__":
    start = float(time.time()) * 1000
    main(sys.argv[1:])
    take_time = float(time.time() * 1000 - start)
    print("Total Time token: %d ms" % take_time)
