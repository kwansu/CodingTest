N, M = map(int, input().split())
cur = int(input())

INF = int(1e9)
adjacency_matrix = []
for i in range(N+1):
    adjacency_matrix.append([INF for _ in range(N+1)])

for _ in range(M):
    s, d, dist = map(int, input().split())
    adjacency_matrix[s][d] = dist

dist_list = [INF]*(N+1)
dist_list[cur] = 0
visit_list = [False]*(N+1)
next = cur

while next:
    min_dist = INF
    cur, next = next, False
    visit_list[cur] = True
    for d in range(1, N+1):
        dist = adjacency_matrix[cur][d] + dist_list[cur]
        if dist_list[d] > dist:
            dist_list[d] = dist
        if visit_list[d]:
            continue
        if min_dist > dist_list[d]:
            min_dist = dist_list[d]
            next = d

for dist in dist_list:
    print(dist)
