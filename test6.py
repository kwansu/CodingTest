import numpy as np
from functools import reduce

directions = ((1, 0), (0, 1), (-1, 0), (0, -1))


def solution(board, r, c):
    # graph = np.zeros([4,4,4,4], dtype=np.int8)
    pos_info = [None] * 13
    pos_info[0] = (r, c)
    for x, line in enumerate(board):
        for y, v in enumerate(line):
            if v == 0:
                continue
            pos_info[v + 6 if pos_info[v] else v] = (x, y)

    def calc_shortest_cost(s, e, remove_info):
        if s == e:
            return 1
        search_list = [s + (2,)]
        visit_list = np.zeros([4, 4], dtype=bool)
        done = True
        while done:
            x, y, cost = search_list.pop(0)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx > 3 or ny < 0 or ny > 3:
                    continue
                if (nx, ny) == e:
                    done = False
                    break
                if not visit_list[nx, ny]:
                    visit_list[nx, ny] = True
                    search_list.append((nx, ny, cost + 1))
                temp = (1 << board[nx][ny]) & (~remove_info-1)
                if temp:
                    continue
                for _ in range(3):
                    nx, ny = nx + dx, ny + dy
                    if nx < 0 or nx > 3 or ny < 0 or ny > 3:
                        nx, ny = nx - dx, ny - dy
                    elif 1 << board[nx][ny] & (~remove_info-1) == 0:
                        continue
                    if visit_list[nx, ny]:
                        break
                    visit_list[nx, ny] = True
                    search_list.append((nx, ny, cost + 1))
                    if (nx, ny) == e:
                        done = False
                    break
                if (nx, ny) == e:
                    break
        return cost

    cache = dict()

    def find_min_cost(si, remove_info):
        if (si, remove_info) in cache:
            return cache[(si, remove_info)]

        min_cost = 10000
        for ki in range(1, 13):
            if 1 << ki & remove_info or not pos_info[ki]:
                continue
            ei = ki - 6 if ki > 6 else ki + 6
            cost = calc_shortest_cost(pos_info[si], pos_info[ki], remove_info)
            cost += calc_shortest_cost(pos_info[ki], pos_info[ei], remove_info)
            cost += find_min_cost(ei, remove_info | (1 << ei) | (1 << ki))
            min_cost = min(min_cost, cost)
        min_cost = min_cost if min_cost < 10000 else 0
        cache[(si, remove_info)] = min_cost
        return min_cost

    return find_min_cost(0, 0)


a = solution([[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]], 1, 0)
print(a)
