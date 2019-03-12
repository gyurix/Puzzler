import abc


class DifCalcStrategy:
    def __init__(self, s2):
        self.s2 = s2
        self.maxx = range(s2.maxx())
        self.maxy = range(s2.maxy())

    @abc.abstractmethod
    def apply(self, s1):
        return 0


class DifCalcIncorrectEP(DifCalcStrategy):
    def apply(self, s1):
        out = 0
        for x in self.maxx:
            for y in self.maxy:
                if s1.data[y][x] != 'm':
                    out += s1.data[y][x] != self.s2.data[y][x]
        return s1.dist + out

    def __repr__(self):
        return 'IncorrectEP'


class DifCalcDistanceFromCorrectEP(DifCalcStrategy):
    def calc_dif(self, s1x, s1y, s1):
        d = s1.data[s1y][s1x]
        if d == 'm' or d == self.s2.data[s1y][s1x]:
            return 0
        for x in self.maxx:
            for y in self.maxy:
                if self.s2.data[y][x] == d:
                    return abs(x - s1x) + abs(y - s1y)

    def apply(self, s1):
        out = 0
        for x in self.maxx:
            for y in self.maxy:
                out += self.calc_dif(x, y, s1)
        return s1.dist + out

    def __repr__(self):
        return 'DistanceFromCorrectEP'
