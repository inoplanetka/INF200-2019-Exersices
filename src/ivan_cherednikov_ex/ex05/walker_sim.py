# -*- coding: utf-8 -*-

__author__ = 'Ivan Cherednikov'
__email__ = 'ivch@nmbu.no'

import random  # import random module


class Walker:
    """
    Class that simulates movement of a person in a one-dimensional world (
    moving along a line)
    """

    def __init__(self, x0, h):
        """
        :param x0 (instead of start): initial position of the walker
        :param h (instead of home): position of walker's home
        """
        self.x0 = x0
        self.x = x0
        self.step = 0
        self.h = h

    def move(self):
        """
        Function for one step
        """
        rnd = random.randint(0, 1)
        if rnd == 0:
            rnd = -1
        self.x += rnd
        self.step += 1

    def is_at_home(self):
        """
        Check if person's at home
        """
        if self.x == self.h:
            return True
        else:
            return False

    def get_position(self):
        """
        Return position
        """
        return self.x

    def get_steps(self):
        """
        Returns amount of steps between start position and end position
        """
        return self.step


def walk_home(x0, h):
    """
    Gets amount steps for a destination and start position
    """
    walk = Walker(x0, h)
    pos = x0

    while pos != h:
        walk.move()
        pos = walk.get_position()
    return walk.get_steps()


class Simulation:

    def __init__(self, start, home, seed):
        """
        Initialise the simulation

        Arguments
        ---------
        start : int
            The walker's initial position
        home : int
            The walk ends when the walker reaches home
        seed : int
            Random generator seed
        """
        self.start = start
        self.home = home
        self.seed = seed

    def single_walk(self):
        """
        Simulate single walk from start to home, returning number of steps.

        Returns
        -------
        int
            The number of steps taken
        """
        walker = Walker(self.start, self.home)

        while not walker.is_at_home():
            walker.move()

        return walker.get_steps()

    def run_simulation(self, num_walks):
        """
        Run a set of walks, returns list of number of steps taken.

        Arguments
        ---------
        num_walks : int
            The number of walks to simulate

        Returns
        -------
        list[int]
            List with the number of steps per walk
        """
        random.seed(self.seed)
        steps_per_sim = [self.single_walk() for _ in range(num_walks)]
        return steps_per_sim


if __name__ == "__main__":

    sim_1 = Simulation(0, 10, 12345)
    sim_2 = Simulation(10, 0, 12345)
    sim_3 = Simulation(0, 10, 54321)
    sim_4 = Simulation(10, 0, 54321)

    l_1 = sim_1.run_simulation(20)
    l_2 = sim_1.run_simulation(20)
    l_3 = sim_2.run_simulation(20)
    l_4 = sim_2.run_simulation(20)
    l_5 = sim_3.run_simulation(20)
    l_6 = sim_4.run_simulation(20)

    print(l_1)
    print(l_2)
    print(l_3)
    print(l_4)
    print(l_5)
    print(l_6)
