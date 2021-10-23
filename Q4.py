N = int(input())
assert(1 <= N <= 1000)

sorted_coins = sorted(list(map(int, input().split())), reverse=True)
assert(len(sorted_coins) == N)

result = 0
n = 0
while n == 0:
    result += 1
    n = result
    for value in sorted_coins:
        if n == value:
            n = 0
            break
        elif n > value:
            n -= value

print(result)
