import abc


class DifCalcStrategy:
    def __init__(self, s2):
        self.s2 = s2

    @abc.abstractmethod
    def apply(self, s1):
        return 0


class DifCalcIncorrectEP(DifCalcStrategy):
    def apply(self, s1):
        out = 0
        for x in range(s1.maxx()):
            for y in range(s1.maxy()):
                if s1.data[y][x] != 'm':
                    out += s1.data[y][x] != self.s2.data[y][x]
        return s1.dist + out


class DifCalcDistanceFromCorrectEP(DifCalcStrategy):
    @staticmethod
    def calc_dif(s1x, s1y, s1, s2, maxx, maxy):
        d = s1.data[s1y][s1x]
        if d == 'm' or d == s2.data[s1y][s1x]:
            return 0
        for x in range(maxx):
            for y in range(maxy):
                if s2.data[y][x] == d:
                    return abs(x - s1x) + abs(y - s1y)

    def apply(self, s1):
        out = 0
        maxx = s1.maxx()
        maxy = s1.maxy()
        for x in range(maxx):
            for y in range(maxy):
                out += self.calc_dif(x, y, s1, self.s2, maxx, maxy)
        return s1.dist + out
