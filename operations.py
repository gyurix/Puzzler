import abc

from state import State


class Operation:
    @abc.abstractmethod
    def apply(self, start):
        return None


class OperationUp(Operation):
    def apply(self, start):
        if start.y == 0:
            return None
        final = State(start)
        final.move(start.x, start.y - 1)
        return final

    def __repr__(self):
        return "Up"


class OperationDown(Operation):
    def apply(self, start):
        if start.y == start.maxy() - 1:
            return None
        final = State(start)
        final.move(start.x, start.y + 1)
        return final

    def __repr__(self):
        return "Down"


class OperationLeft(Operation):
    def apply(self, start):
        if start.x == 0:
            return None
        final = State(start)
        final.move(start.x - 1, start.y)
        return final

    def __repr__(self):
        return "Left"


class OperationRight(Operation):
    def apply(self, start):
        if start.x == start.maxx() - 1:
            return None
        final = State(start)
        final.move(start.x + 1, start.y)
        return final

    def __repr__(self):
        return "Right"


operations = [OperationLeft(), OperationRight(), OperationUp(), OperationDown()]
