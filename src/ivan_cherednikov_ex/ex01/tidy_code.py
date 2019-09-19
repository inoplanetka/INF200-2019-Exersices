from random import randint as dice

__author__ = 'Ivan Cherednikov'
__email__ = 'ivch@nmbu.no'


def guess_input():
    guess = 0
    while guess < 2:
        guess = int(input('Your guess: '))
    return guess

def dice_roll():
    return dice(1, 6) + dice(1, 6)

def compare_sum_with_guess(sum_eyes, your_guess):
    return sum_eyes == your_guess

if __name__ == '__main__':

    win = False
    attempts = 3
    sum_eyes = dice_roll()
    while not win and attempts > 0:
        your_guess = guess_input()
        win = compare_sum_with_guess(sum_eyes, your_guess)
        if not win:
            print('Wrong, try again!')
            attempts -= 1

    if attempts > 0:
        print('You won {} points.'.format(attempts))
    else:
        print('You lost. Correct answer: {}.'.format(sum_eyes))