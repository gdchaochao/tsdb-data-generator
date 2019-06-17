# coding=utf-8

import random


# 状态位Provider
class StatusProvider(object):
    def __init__(self, range_start, range_end, len_byte=1, error_status=True):
        """
        初始化
        :param range_start: 随机数字开始
        :param range_end: 随机数字结束
        :param len_byte: 占用的字节数
        :param error_status: 随机数是否需要包含异常位
        """
        self.range_start = range_start
        self.range_end = range_end
        self.error_status = error_status
        self.range_list = list(range(range_start, range_end + 1))
        if error_status:
            if len_byte == 1:
                self.range_list.append(0xfe)
                self.range_list.append(0xff)
            elif len_byte == 2:
                self.range_list.append(0xfffe)
                self.range_list.append(0xffff)
            elif len_byte == 4:
                self.range_list.append(0xfffffffe)
                self.range_list.append(0xffffffff)

    def random_status(self):
        value = random.choice(self.range_list)
        return value


if __name__ == "__main__":
    sp = StatusProvider(1, 4, len_byte=2)
    print(sp.random_status())
