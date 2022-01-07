import time
from itertools import combinations


def get_combination(set_list, n):
    if n == 1:
        return set_list
    
    result = []
    for i, c in enumerate(set_list[:-n+1],1):
        local_result = get_combination(set_list[i:], n-1)
        result.extend([c + combo for combo in local_result])

    return result

items = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
iter_num = 10

start = time.time()
for _ in range(iter_num):
    a = get_combination(items, 2)
print(time.time() - start)

start = time.time()
for _ in range(iter_num):
    b = list(combinations(items, 2))
print(time.time() - start)

print(b)