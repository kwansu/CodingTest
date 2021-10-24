N = int(input())
assert(3 <= N <= 100)

foods = list(map(int, input().split()))
assert(len(foods) == N)


before_use = 0
before_skip = 0
for n in foods:
    # 이번 창고를 털경우
    temp = before_skip + n
    # 창고를 안털 경우
    if before_use > before_skip:
        before_skip = before_use
    
    before_use = temp

print(max(before_use, before_skip))