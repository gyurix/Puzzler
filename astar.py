from sortedcontainers import SortedDict

from operations import operations


def a_star_solve(s1, strategy):
    s2 = strategy.s2
    open_list = SortedDict(strategy.apply)
    open_list[s1] = s1
    closed_list = set()
    while True:
        cur = open_list._list_pop(0)
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
                old = open_list.get(nbor)
                if old is None or old.dist > nbor.dist:
                    open_list[nbor] = nbor
