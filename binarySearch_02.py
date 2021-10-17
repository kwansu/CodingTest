N = int(input())
items = list(map(int, input().split()))
assert(1 <= N <= 100000 and len(items) == N)
M = int(input())
orders = list(map(int, input().split()))
assert(1 <= M <= 100000 and len(orders) == M)

items.sort()

def is_in(target_value, items):
    s, e = 0, len(items)-1
    while s <= e:
        m = (s+e) // 2
        temp = items[m]
        if temp == target_value:
            return True
        if temp > target_value:
            e = m - 1
        else:
            s = m + 1
    return False


result = True
for id in orders:
    print('yes' if is_in(id, items) else 'no')
