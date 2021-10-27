N, M = map(int, input().split())
assert(1 <= N <= 100)
assert(1 <= M <= 10000)

coins = []
for _ in range(N):
    coins.append(int(input()))

coins.sort()


uncheck_list = [True]*(M+1)
cur_list = [M]
result = 0
has_answer = False
while len(cur_list) != 0:
    result += 1
    for _ in range(len(cur_list)):
        if has_answer:
            break
        m = cur_list.pop(0)
        for coin in coins: # 이진탐색으로 변경하면 더 좋을듯
            if m == coin:
                cur_list.clear()
                has_answer = True
                break
            elif m < coin:
                break
            temp = m - coin
            if uncheck_list[temp]:
                uncheck_list[temp] = False
                cur_list.append(temp)

print(result if has_answer else -1)
