import abc

from state import State


class Operation:
    @abc.abstractmethod
    def apply(self, start):
        return


class OperationUp(Operation):
    def apply(self, start):
        if start.y == 0:
            return start
        final = State(start)
        final.move(start.x, start.y - 1)
        return final


class OperationDown(Operation):
    def apply(self, start):
        if start.y == start.maxy() - 1:
            return start
        final = State(start)
        final.move(start.x, start.y + 1)
        return final


class OperationLeft(Operation):
    def apply(self, start):
        if start.x == 0:
            return start
        final = State(start)
        final.move(start.x - 1, start.y)
        return final


class OperationRight(Operation):
    def apply(self, start):
        if start.x == start.maxx() - 1:
            return start
        final = State(start)
        final.move(start.x + 1, start.y)
        return final


operations = [OperationLeft(), OperationRight(), OperationUp(), OperationDown()]
