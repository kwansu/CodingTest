import heapq

INF = int(1e9)
# N, M = map(int, input().split())

# adjacency_list = [[] for _ in range(N+1)]
# for _ in range(M):
#     s, d = map(int, input().split())
#     adjacency_list[s].append(d)

# X, K = map(int, input().split())

N, M = 5, 7
adjacency_list = [[] for _ in range(N+1)]
adjacency_list[1].extend([2, 3, 4])
adjacency_list[2].extend([1, 4])
adjacency_list[3].extend([1, 4, 5])
adjacency_list[4].extend([1, 2, 3, 5])
adjacency_list[5].extend([3, 4])
X, K = 4, 5


def calc_shortest_path(start, dest):
    shortest_path_list = [INF] * (N+1)
    visit_list = [False] * (N+1)
    priority_list = [(0, start)]

    while priority_list:
        cost, cur = heapq.heappop(priority_list)
        if visit_list[cur]:
            continue
        visit_list[cur] = True
        if cur == dest:
            break

        for next in adjacency_list[cur]:
            if shortest_path_list[next] > cost+1:
                heapq.heappush(priority_list, (cost+1, next))
                shortest_path_list[next] = cost+1

    return -1 if shortest_path_list[dest] == INF else shortest_path_list[dest]


result = calc_shortest_path(1, K)
if result != -1:
    temp = calc_shortest_path(K, X)
    result = result + temp if temp != -1 else -1

print(result)    
    