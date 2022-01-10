from collections import defaultdict

N = 5
LINE = [(0, 1, 2), (1, 2, 1), (1, 3, 7), (3, 4, 5)]

costs = [0 for _ in range(N)]
counts = [0 for _ in range(N)]
edges = defaultdict(list)


def update_cost(s, e, count, cost, total):
    total += cost * count
    costs[e] += total
    counts[e] += count
    for t, c in edges[e]:
        if s != t:
            update_cost(e, t, count, c, total)


for u, v, c in LINE:
    t_count, t_cost = counts[v], costs[v]
    update_cost(u, v, counts[u] + 1, c, costs[u])
    update_cost(v, u, t_count + 1, c, t_cost)
    edges[u].append((v, c))
    edges[v].append((u, c))

min_cost = int(1e9)
for i in range(N):
    min_cost = min(min_cost, costs[i])

print(min_cost)
