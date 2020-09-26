# -*- coding: utf-8 -*-
from functools import reduce


class Calc:
    def add(self, *args):
        return sum(args)

    def sub(self, a, b):
        return a - b

    def mul(self, *args):
        if not all(args):
            raise ValueError
        return reduce(lambda x, y: x * y, args)

    def div(self, a, b):
        # if not b:
        #     return "inf"
        # return a / b

        try:
            return a / b
        except ZeroDivisionError:
            return "inf"

    def avg(self, it):
        return sum(it) / len(it)
