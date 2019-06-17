# coding=utf-8

from faker import Faker


# 状态位Provider
class VINProvider(object):
    def __init__(self):
        self.fake = Faker()

    def random_status(self):
        return self.fake.password(length=17, special_chars=False, digits=True, upper_case=True, lower_case=False)


if __name__ == "__main__":
    sp = VINProvider(1)
    print(sp.random_status())
