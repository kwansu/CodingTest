N = int(input())
assert(1 <= N <= 30000)

uncheck_list = [True] * 30000
cur_list = [N]


def check_and_append(n, mod):
    if mod == 0 and uncheck_list[n]:
        uncheck_list[n] = False
        cur_list.append(n)


result = -1
n = N
while n > 1:
    result += 1
    for _ in range(len(cur_list)):
        n = cur_list.pop(0)
        if n == 1:
            break
        check_and_append(n-1, 0)
        check_and_append(*divmod(n, 5))
        check_and_append(*divmod(n, 3))
        check_and_append(*divmod(n, 2))

print(result)