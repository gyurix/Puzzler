from sortedcontainers import SortedSet

from operations import operations


def a_star_solve(s1, strategy):
    s2 = strategy.s2
    open_list = SortedSet([s1], strategy.apply)
    closed_list = set()
    while True:
        cur = open_list.pop(0)
        if cur == s2:
            out = [cur]
            while cur.parent is not None:
                out.append(cur.parent)
                cur = cur.parent
            out.reverse()
            return out
        else:
            closed_list.add(cur)
            for op in operations:
                nbor = op.apply(cur)
                if nbor is None or nbor in closed_list:
                    continue
                # if nbor in open_list:
                #    if cur.dist < nbor.dist:
                #        del open_list[open_list.index(nbor)]
                #        open_list.add(nbor)
                # else:
                open_list.add(nbor)
