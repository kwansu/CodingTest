N, M = map(int, input().split())

grid = []
for n in range(N):
    line = list(map(int, list(input())))
    assert(len(line) == M)
    grid.append(line)

def dfs(x, y):
    grid[x][y] = 2
    if x > 1 and grid[x-1][y] == 0:
        dfs(x-1, y)
    if x < N-1 and grid[x+1][y] == 0:
        dfs(x+1, y)
    if y > 1 and grid[x][y-1] == 0:
        dfs(x, y-1)
    if y < M-1 and grid[x][y+1] == 0:
        dfs(x, y+1)

result = 0
for i in range(N):
    for j in range(M):
        if grid[i][j] == 0:
            dfs(i, j)
            result += 1

print(result)
