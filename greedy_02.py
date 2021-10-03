line1 = '5 7 2'
line2 = '3 4 3 4 3'

N, M, K = map(int, line1.split())
num_list = list(map(int, line2.split()))

assert(len(num_list) == N)
assert(K <= M)

max1 = max(num_list)
num_list.remove(max1)
max2 = max(num_list)

max2_count = M // (K+1)
result = max1 * (M - max2_count) + max2 * max2_count

print(f"동빈이의 큰 수의 법칙에 따른 답 : {result}")
