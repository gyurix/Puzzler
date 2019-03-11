class State:
    def __init__(self, prev=None):
        if prev is None:
            self.data = None
            self.prev = None
            self.x = self.y = 0
            self.dist = 0
            return
        self.dist = prev.dist + 1
        self.data = prev.data
        self.x = prev.x
        self.y = prev.y

    def move(self, x, y):
        self.data[self.y][self.x] = self.data[y][x]
        self.data[y][x] = 'm'
        self.x = x
        self.y = y
        return

    def maxx(self):
        return len(self.data[0])

    def maxy(self):
        return len(self.data)

    def find_pos(self):
        self.y = 0
        for d in self.data:
            try:
                self.x = d.index('m')
                return
            except ValueError:
                self.y += 1

    def read_data(self):
        self.data = eval(
            input().replace(' ', ',').replace(')(', '],[').replace('m', "'m'").replace('(', '[').replace(')', ']'))
        self.find_pos()
        return self

    def __eq__(self, other):
        return self.data == other.data

    def __str__(self):
        out = '('
        for row in self.data:
            out += str(row).replace(', ', ' ').replace("'", '').replace('[', '(').replace(']', ')')
        return out + ')'
