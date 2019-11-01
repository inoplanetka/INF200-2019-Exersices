# -*- coding: utf-8 -*-

__author__ = 'Ivan Cherednikov'
__email__ = 'ivch@nmbu.no'


class LCGRand:
    def __init__(self, seed):
        self.a = 16807
        self.m = (2 ** 31) - 1
        self.r = seed

    def rand(self):
        self.r = self.a*self.r % self.m
        return self.r


class ListRand:
    def __init__(self, numbers):
        self.numbers = numbers
        self.idx = 0

    def rand(self):
        if self.idx >= len(self.numbers): # hopefully this line is correct
            raise RuntimeError
        else:
            self.idx += 1
            return self.numbers[self.idx - 1]


if __name__ == "__main__":
    lcg = LCGRand(241)
    lrList = [4, 10, 5, 8, 6, 15]
    lr = ListRand(lrList)
    lcg_numb = []
    lr_numb = []
    for i in range(10):
        lcg_numb.append(lcg.rand())

    for i in range(len(lrList)):
        lr_numb.append(lr.rand())

    print(lcg_numb)
    print(lr_numb)
