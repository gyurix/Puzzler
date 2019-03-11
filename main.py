import astar
from difcalc import *
from state import State

s1 = State().read_data()
s2 = State().read_data()
for s in astar.a_star_solve(s1, DifCalcIncorrectEP(s2)):
    print(s)
