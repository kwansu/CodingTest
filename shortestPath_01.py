import heapq

INF = int(1e9)
# N, M = map(int, input().split())
# start_node = int(input())

# adjacency_list = [[] for _ in range(N+1)]

# for _ in range(M):
#     src, dest, cost = map(int, input().split())
#     adjacency_list[src].append((dest, cost))

N, M = 6, 11
start_node = 1
adjacency_list = [[]]
adjacency_list.append([(2, 2), (3, 5), (4, 1)])
adjacency_list.append([(3, 3), (4, 2)])
adjacency_list.append([(2, 3), (6, 5)])
adjacency_list.append([(3, 3), (5, 1)])
adjacency_list.append([(3, 1), (6, 2)])
adjacency_list.append([])

shortest_path_list = [INF] * (N+1)
shortest_path_list[start_node] = 0
visit_list = [False] * (N+1)
next = start_node

while next:
    cur, next = next, False
    visit_list[cur] = True
    for dest, cost in adjacency_list[cur]:
        cost += shortest_path_list[cur]
        if shortest_path_list[dest] > cost:
            shortest_path_list[dest] = cost

    min_cost = INF
    for i in range(1, N+1):
        if not visit_list[i] and min_cost > shortest_path_list[i]:
            min_cost, next = shortest_path_list[i], i

for cost in shortest_path_list[1:]:
    print(cost)


shortest_path_list = [INF] * (N+1)
shortest_path_list[start_node] = 0
visit_list = [False] * (N+1)
heap = [(0, 1)]

while len(heap) > 0:
    cost, cur = heapq.heappop(heap)
    if visit_list[cur]:
        continue
    visit_list[cur] = True

    for dest, cost in adjacency_list[cur]:
        cost += shortest_path_list[cur]
        if shortest_path_list[dest] > cost:
            shortest_path_list[dest] = cost
            heapq.heappush(heap, (cost, dest))

for cost in shortest_path_list[1:]:
    print(cost)