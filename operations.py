import abc

from state import State


class Operation:
    @abc.abstractmethod
    def apply(self, start):
        return


class OperationUp(Operation):
    def apply(self, start):
        final = State(start)
        return final


class OperationDown(Operation):
    def apply(self, start):
        final = State(start)
        return final


class OperationLeft(Operation):
    def apply(self, start):
        final = State(start)
        return final


class OperationRight(Operation):
    def apply(self, start):
        final = State(start)
        return final


operations = [OperationLeft(), OperationRight(), OperationUp(), OperationDown()]
