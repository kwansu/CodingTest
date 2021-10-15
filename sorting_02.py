N = int(input())

result = []
result.append(int(input()))

# 삽입 정렬
for _ in range(N-1):
    num = int(input())

    if num >= result[-1]:
        result.append(num)
        continue

    for i,n in enumerate(result):
        if n >= num:
            result.insert(i, num)
            break

print(result)