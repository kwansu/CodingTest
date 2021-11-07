N, M = 7, 8
commands = []
commands.append((0, 1, 3))
commands.append((1, 1, 7))
commands.append((0, 7, 6))
commands.append((1, 7, 1))
commands.append((0, 3, 7))
commands.append((0, 4, 2))
commands.append((0, 1, 1))
commands.append((1, 1, 1))

root_list = [n for n in range(N+1)]

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

    
for c, a, b in commands:
    if c == 0:
        union(a, b)
    else:
        print(find_root(a) == find_root(b))
