N, M = map(int, input().split())
assert(1 <= N <= 1000000 and 1 <= M <= 2000000000)

lengths = sorted(list(map(int, input().split())), reverse=True)
assert(N == len(lengths))


def calc_sum(i):
    return sum(lengths[:i+1]) - lengths[i] * (i+1)


start, end = 0, N-1
while end >= start:
    mid = (start + end) // 2
    total = calc_sum(mid)
    if total == M:
        break
    elif total > M:
        end = mid - 1
    else:
        start = mid + 1

if total - M < 0:
    result = lengths[mid] + (total - M) // (mid + 1)
else:
    result = lengths[mid] + (total - M) // mid

print(result)


total = 0
min = lengths[0]
dist = 0
n = 0
idx = 0
for len in lengths:
    if min > len:
        dist = min - len
        min = len
        n = idx

    total += n * dist
    if total >= M:
        break

    idx += 1

result = min + (total - M) // idx
print(result)
