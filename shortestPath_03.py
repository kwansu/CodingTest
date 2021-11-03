import heapq

INF = int(1e9)
N, M, C = map(int, input().split())
assert(1 <= N <= 30000 and 1 <= M <= 200000 and 1 <= C <= N)

adjacency_list = [[] for _ in range(N+1)]
for _ in range(M):
    x, y, z = map(int, input().split())
    assert(1 <= x <= N and 1 <= y <= N and 1 <= z <= 1000)
    adjacency_list[x].append((y, z))


cost_sum = 0
heap = [(0, C)]
visit_list = [False] * (N+1)
while heap:
    cost_sum, start = heapq.heappop(heap)
    
    if visit_list[start]:
        continue
    visit_list[start] = True

    for dest, cost in adjacency_list[start]:
        cost += cost_sum
        heapq.heappush(heap, (cost, dest))

print(f'받은 도시수 : {sum(visit_list)-1}, 최소 시간 : {cost_sum}')