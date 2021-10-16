N, K = map(int, input().split())
assert(1 <= N <= 1000000 and 1 <= K <= 1000000)

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

for _ in range(K):
    if A[0] < B[-1]:
        a, b = A.pop(0), B.pop()
        A.append(b)

print(sum(A))