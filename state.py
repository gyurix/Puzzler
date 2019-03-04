class State:
    def __init__(self, prev=None):
        self.data = None
        self.pos = None
        self.prev = prev

    def find_pos(self):
        y = 0
        for d in self.data:
            try:
                x = d.index('m')
                self.pos = (x, y)
                return
            except ValueError:
                y += 1

    def read_data(self):
        self.data = eval(input().replace(' ', ',').replace(')(', '),(').replace('m', "'m'"))
        self.find_pos()
        return self

    def __str__(self):
        out = '('
        for row in self.data:
            out += str(row).replace(', ', ' ').replace("'", '')
        return out + ')'
