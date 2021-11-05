# 서로소 집합
N, M = 6, 4
unions = [(1, 4), (2, 3), (2, 4), (5, 6)]


def find_root(n):
    if parent_info[n] != n:
        parent_info[n] = find_root(parent_info[n])
    return parent_info[n]


parent_info = [n for n in range(N+1)]

for a, b in unions:
    p, c = (a, b) if find_root(a) < find_root(b) else (b, a)
    temp = find_root(p)
    parent_info[c] = temp


print([find_root(n) for n in range(1, N+1)])
print(parent_info[1:])