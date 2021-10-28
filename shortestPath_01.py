INF = int(1e9)
# N, M = map(int, input().split())
# cur = int(input())

# adjacency_list = [[] for _ in range(N+1)]

# for _ in range(M):
#     start, dest, dist = map(int, input().split())
#     adjacency_list[start].append((dest, dist))

N, M = 6, 11
cur = 1
adjacency_list = [[]]
adjacency_list.append([(2, 2), (3, 5), (4, 1)])
adjacency_list.append([(3, 3), (4, 2)])
adjacency_list.append([(2, 3), (6, 5)])
adjacency_list.append([(3, 3), (5, 1)])
adjacency_list.append([(3, 1), (6, 2)])
adjacency_list.append([])

dist_list = [INF]*(N+1)
dist_list[cur] = 0
visit_list = [False]*(N+1)
next = cur

while next:
    cur, next = next, False
    visit_list[cur] = True
    for dest, dist in adjacency_list[cur]:
        dist += dist_list[cur]
        if dist_list[dest] > dist:
            dist_list[dest] = dist

    min_dist = INF
    for i in range(1, N+1):
        if not visit_list[i] and min_dist > dist_list[i]:
            min_dist, next = dist_list[i], i

for dist in dist_list[1:]:
    print(dist)
