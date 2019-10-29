# -*- coding: utf-8 -*-

__author__ = 'Ivan Cherednikov'
__email__ = 'ivch@nmbu.no'

import random


class Walker:
    def __init__(self, x0, y):
        self.x = x0
        self.y = y
        self.n = 0

    def move(self):
        stepval = random.randint(1, 2)
        if stepval == 1:
            self.x -= 1
        else:
            self.x += 1
        self.n += 1

    def is_at_home(self):
        if self.x == self.y:
            return True

    def get_position(self):
        return self.x

    def get_steps(self):
        return self.n


if __name__ == "__main__":
    homes = [1, 2, 5, 10, 20, 50, 100]
    start = 0
    home_steps = {}
    for home in homes:
        temp_home_steps = []
        for x in range(5):
            walk = Walker(start, home)
            while not walk.is_at_home():
                walk.move()
            temp_home_steps.append(walk.get_steps())
        home_steps[home] = temp_home_steps

    for x in homes:
        print('Distance: {} --> path lengths: {}'.format(x, home_steps[x]))
