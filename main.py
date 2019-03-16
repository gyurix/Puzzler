from math import log10

import astar
from difcalc import *
from state import State


def print_path(path):
    """
        Prints the given path to the standard output
        :param path: The printable path (list of State objects)
        :return: None
    """
    print('\nPath len =', len(path))
    i = 0
    fmt = '{:' + str(int(log10(len(path) * 10 - 1))) + '}. {}'
    for s in path:
        print(fmt.format(i, s.__repr__()))
        i += 1


if __name__ == '__main__':
    while True:
        s1 = State().load_data(input('From: '))
        s2 = State().load_data(input('To: '))

        print_path(astar.a_star_solve(s1, DifCalcIncorrectEP(s2)))
