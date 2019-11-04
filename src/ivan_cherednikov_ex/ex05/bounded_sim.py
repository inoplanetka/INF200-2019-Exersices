# -*- coding: utf-8 -*-

__author__ = 'Ivan Cherednikov'
__email__ = 'ivch@nmbu.no'


from walker_sim import Walker, Simulation


class BoundedWalker(Walker):
    def __init__(self, start, home, left_limit, right_limit):
        """
        Initialise the walker

        Arguments
        ---------
        start : int
            The walker's initial position
        home : int
            The walk ends when the walker reaches home
        left_limit : int
            The left boundary of walker movement
        right_limit : int
            The right boundary  of walker movement
        """
        super().__init__(start, home)
        self.left_limit = left_limit
        self.right_limit = right_limit
        self.x = start

    def valid_position(self):
        super().move()
        if self.x < self.left_limit:
            self.x = self.left_limit
            self.step -= 1
        if self.x > self.right_limit:
            self.step -= 1
            self.x = self.right_limit


class BoundedSimulation(Simulation):
    def __init__(self, start, home, seed, left_limit, right_limit):
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
        left_limit : int
            The left boundary of walker movement
        right_limit : int
            The right boundary  of walker movement
        """
        super().__init__(start, home, seed)
        self.right_limit = right_limit
        self.left_limit = left_limit

    def bounded_single_walk(self):
        b_walker = BoundedWalker(self.start, self.home,
                                 self.left_limit, self.right_limit)
        while not b_walker.is_at_home():
            b_walker.valid_position()

        return b_walker.get_steps()


if __name__ == "__main__":
    cond_1 = BoundedSimulation(0, 20, 12345, 0, 20)
    cond_2 = BoundedSimulation(0, 20, 12345, -10, 20)
    cond_3 = BoundedSimulation(0, 20, 12345, -100, 20)
    cond_4 = BoundedSimulation(0, 20, 12345, -1000, 20)
    cond_5 = BoundedSimulation(0, 20, 12345, -10000, 20)

    print(cond_1.run_simulation(20))
    print(cond_2.run_simulation(20))
    print(cond_3.run_simulation(20))
    print(cond_4.run_simulation(20))
    print(cond_5.run_simulation(20))
