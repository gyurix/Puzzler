class State:
    def __init__(self, parent=None):
        self.created_nodes = 0
        self.parent = parent
        if parent is None:
            self.data = None
            self.prev = None
            self.x = self.y = 0
            self.dist = 0
            return
        self.dist = parent.dist + 1
        self.data = [x[:] for x in parent.data]
        self.x = parent.x
        self.y = parent.y

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

    def load_data(self, data):
        self.data = eval(
            data.replace(' ', ',').replace(')(', '],[').replace('m', "'m'").replace('(', '[').replace(')', ']'))
        self.find_pos()
        return self

    def __eq__(self, other):
        return self.data == other.data

    def __str__(self):
        out = '('
        for row in self.data:
            out += str(row).replace(', ', ' ').replace("'", '').replace('[', '(').replace(']', ')')
        return out + ')'

    def __repr__(self):
        return self.__str__() + ' {dist=' + str(self.dist)+'; created nodes='+str(self.created_nodes)+'}'

    def __hash__(self):
        out = 0
        for row in self.data:
            for col in row:
                out = out * 17 + (11 if col == 'm' else col)
        return out
