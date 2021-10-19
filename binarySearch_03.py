N, M = map(int, input().split())
assert(1 <= N <= 1000000 and 1 <= M <= 2000000000)

lengths = sorted(list(map(int, input().split())), reverse=True)
assert(N == len(lengths))


####################### 방법 1 ###################################
def calc_sum(i):
    return sum(lengths[:i+1]) - lengths[i] * (i+1)


start, end = 0, N-1
a, b = start, end
while end >= start:
    mid = (start + end) // 2
    total = calc_sum(mid)
    if total == M:
        break
    elif total > M:
        end = mid - 1
    else:
        start = mid + 1

result = lengths[mid] + (total - M) // (mid + (1 if total - M < 0 else 0))
print(result)

###################### 방법 2 ##############################


def calc_variation(a, b, dir):
    return dir * sum(lengths[a:b+1]) - lengths[b]*(b+1 - a) + (lengths[a] + lengths[b])*a


start, end = 0, N-1
a, b = start, end
dir = 1
total = 0
while end >= start:
    total += calc_variation(a, b, dir)
    if total == M:
        break
    elif total > M:
        end = mid
        mid = (start + end) // 2
        a, b, dir = mid, end, -1
    else:
        start = mid
        mid = (start + end) // 2
        a, b, dir = start, mid, 1


result = lengths[mid] + (total - M) // (mid + (1 if total - M < 0 else 0))
print(result)


####################### 방법 3 ######################
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
