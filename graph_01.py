# 서로소 집합
N, M = 6, 4
unions = [(1, 4), (2, 3), (2, 4), (5, 6)]


def find_root(n):
    if root_list[n] != n:
        root_list[n] = find_root(root_list[n])
    return root_list[n]


root_list = [n for n in range(N+1)]

for a, b in unions:
    p, c = (a, b) if root_list[a] < root_list[b] else (b, a)
    root_list[c] = find_root(p)


print([find_root(n) for n in range(1, N+1)])
print(root_list[1:])


# 신장 트리
N, M = 7, 9
edge_list = []
edge_list.append((1, 2, 29))
edge_list.append((1, 5, 75))
edge_list.append((2, 3, 35))
edge_list.append((2, 6, 34))
edge_list.append((3, 4, 7))
edge_list.append((4, 6, 23))
edge_list.append((4, 7, 13))
edge_list.append((5, 6, 53))
edge_list.append((6, 7, 25))
edge_list.sort(key=lambda x: x[2])
root_list = [n for n in range(N+1)]


mst = []
for n1, n2, cost in edge_list:
    p, c = find_root(n1), find_root(n2)
    if p == c:
        continue
    if p < c:
        root_list[c] = p
    else:
        root_list[p] = c
    mst.append((n1, n2, cost))


print(sum([x[2] for x in mst]))


# 위상 정렬
N, M = 7, 8
indegree_list = [0] * (N+1)
adjacency_list = [[] for _ in range(N+1)]

def create_edge(s, e):
    indegree_list[e] += 1
    adjacency_list[s].append(e)


create_edge(1, 2)
create_edge(1, 5)
create_edge(2, 3)
create_edge(2, 6)
create_edge(3, 4)
create_edge(4, 7)
create_edge(5, 6)
create_edge(6, 4)

cur_queue = [i for i, n in enumerate(indegree_list[1:], start=1) if n == 0]
sorted_nodes = []

while cur_queue:
    n = cur_queue.pop(0)
    sorted_nodes.append(n)
    for e in adjacency_list[n]:
        indegree_list[e] -= 1
        if indegree_list[e] == 0:
            cur_queue.append(e)


print(sorted_nodes)