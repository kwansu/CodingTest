N, M = 7, 12

edge_list = []
edge_list.append((1, 2, 3))
edge_list.append((1, 3, 2))
edge_list.append((3, 2, 1))
edge_list.append((2, 5, 2))
edge_list.append((3, 4, 4))
edge_list.append((7, 3, 6))
edge_list.append((5, 1, 5))
edge_list.append((1, 6, 2))
edge_list.append((6, 4, 1))
edge_list.append((6, 5, 3))
edge_list.append((4, 5, 3))
edge_list.append((6, 7, 4))

root_list = [n for n in range(N+1)]
edge_list.sort(key=lambda t: t[2])


def find_root(n):
    if root_list[n] != n:
        root_list[n] = find_root(root_list[n])
    return root_list[n]


def union(a, b):
    a = find_root(a)
    b = find_root(b)
    if a < b:
        root_list[b] = a
    else:
        root_list[a] = b

result = 0
last_cost = 0
for a, b, cost in edge_list:
    if find_root(a) != find_root(b):
        union(a, b)
        result += cost
        last_cost = cost

if sum(root_list[1:]) == root_list[1]*N:
    result -= last_cost

print(result)