from sortedcontainers import SortedDict

from operations import operations


def a_star_solve(s1, strategy):
    """
        Finds a valid path for reaching the final state from the initial state
        :param s1: The initial state
        :param strategy: The heuristic strategy, including the final state (as it's s2 attribute)
        :return: The list of States we need to go through for reaching the final state from the initial one
    """
    # Our final state will be the heuristic strategies s2 attribute
    s2 = strategy.s2

    # Using SortedDict from sorted containers library for getting O(log n) time complexity
    # at both element adding, element getting and removing the smallest element operations
    # O(1) remove first element complexity
    open_list = SortedDict(strategy.apply)

    # Add the initial state to the open list
    open_list[s1] = s1

    # Counter for the created nodes, used as a key indicator for collecting data about heuristic strategies performance
    created_nodes = 0

    # Closed list is a regular Python set for getting O(1) time complexity at both
    # element adding and element getting operations
    closed_list = set()

    while True:
        # The currently checked state will be the one having the smallest f score
        # g score = length of path towards reaching the state from the initial state
        # h score = estimated remaining path length for reaching the final state from the current state
        # f score = g score + h score
        cur = open_list._list_pop(0)
        if cur == s2:
            # If we have reached the final state, construct a list of states of the valid path
            # we found.
            #
            # We do it by going through the current paths parents and adding them to the beginning
            # of the list of states we want to return
            out = [cur]
            while cur.parent is not None:
                out.append(cur.parent)
                cur = cur.parent
            out.reverse()
            return out
        else:
            # If we have not reached the final state yet, add the currently checked state to the closed list
            # for ensuring we will process it only once
            closed_list.add(cur)
            for op in operations:
                # Try applying all the neighbour generator operations on the current state
                # for finding it's valid neighbours
                nbor = op.apply(cur)
                if nbor is None or nbor in closed_list:
                    continue
                # If we have found a valid neighbour, that is not on closed_list we increase the created node count
                # and process our neighbour
                created_nodes += 1
                nbor.created_nodes = created_nodes
                nbor.op = op
                old = open_list.get(nbor)
                # If the neighbour is already in open list, but with higher f score, then we replace it with
                # the currently found one having the lower f score.
                # If the neighbour is not in the open list yet, then we add it to it
                if old is None or old.dist > nbor.dist:
                    open_list[nbor] = nbor
