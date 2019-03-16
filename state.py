class State:
    """
        One state of the puzzle, including the following information:
        - parent: The state from which we got into this one
        - created nodes: Amount of states created during the execution of the path finding algorithm
                         for getting into this state (used for measuring heuristic remaining path length
                         calculator algorithms performance)
        - x,y: Coordinates of 'm', which can be moved in 4 directions for finding this states neighbours
        - data: 2D data array of numbers of the puzzle
        - dist: The depth of parents of this state
    """

    def __init__(self, parent=None):
        """
            Initializes this state (with no data if no parent is provided)
            :param parent: Optional parent argument (the data will be copied from the parent, if it's provided)
        """
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
        """
            Moves the 'm' to the target x and y location, replaces the number on it's current location with the
            current number in it's new location
            :param x: Target x location
            :param y: Target y location
            :return: None
        """
        self.data[self.y][self.x] = self.data[y][x]
        self.data[y][x] = 'm'
        self.x = x
        self.y = y

    def maxx(self):
        """
            Gets the width (maxx) of the data
            :return: The width of the data
        """
        return len(self.data[0])

    def maxy(self):
        """
            Gets the height (maxy) of the data
            :return: The height of the data
        """
        return len(self.data)

    def find_pos(self):
        """
            Finds the x and y positions of the m.
            Used at loading data
            :return: None
        """
        self.y = 0
        for d in self.data:
            try:
                self.x = d.index('m')
                return
            except ValueError:
                self.y += 1

    def load_data(self, data):
        """
            Loads the data of this stage from a String
            :param data: The String containing the loadable data in a ((1 2 3)(4 5 6)(7 8 m)) format
            :return: This state
        """
        self.data = eval(
            data.replace(' ', ',').replace(')(', '],[').replace('m', "'m'").replace('(', '[').replace(')', ']'))
        self.find_pos()
        return self

    def __eq__(self, other):
        """
            Compares this state with another state. Two states equals if their data equals.
            :param other: The state which we want to compare this state with
            :return: True if the two states are equal, False otherwise
        """
        return self.data == other.data

    def __str__(self):
        """
            Converts this state to a ((1 2 3)(4 5 6)(7 8 m)) formatted String
            :return: The conversion result
        """
        out = '('
        for row in self.data:
            out += str(row).replace(', ', ' ').replace("'", '').replace('[', '(').replace(']', ')')
        return out + ')'

    def __repr__(self):
        """
            Generates the String showing the significant fields of this states, which includes it's
            data in a ((1 2 3)(4 5 6)(7 8 m)) format, it's dist and the created nodes
            :return: The generated String
        """
        return self.__str__() + ' {dist=' + str(self.dist) + '; created nodes=' + str(self.created_nodes) + '}'

    def __hash__(self):
        """
            Generates a hash code from this states data, for being able to add it to hash sets having O(1) complexity
            :return: The generation result
        """
        out = 0
        for row in self.data:
            for col in row:
                out = out * 17 + (11 if col == 'm' else col)
        return out
