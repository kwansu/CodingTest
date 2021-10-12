N, M = map(int, input().split())

grid = []
for n in range(N):
    line = list(map(int, list(input())))
    assert(len(line) == M)
    grid.append(line)


def check_grid(x, y, leafs):
    if x >= 0 and x < N and y >= 0 and y < M:
        if grid[x][y] == 1:
            grid[x][y] = 0
            leafs.append((x, y))
            return True
    return False


grid[0][0] = 0
goal = (N-1, M-1)
leafs = [(0, 0)]
result = 0

while len(leafs) != 0:
    result += 1
    next_leafs = []
    for leaf in leafs:
        if leaf == goal:
            break
        x, y = leaf
        check_grid(x+1, y, next_leafs)
        check_grid(x, y+1, next_leafs)
        check_grid(x-1, y, next_leafs)
        check_grid(x, y-1, next_leafs)
    
    leafs = next_leafs

print(result)