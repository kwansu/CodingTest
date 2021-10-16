N = int(input())

sorted_list = []
for n in range(N):
    name, score = input().split()
    sorted_list.append((name, int(score)))

sorted_list.sort(key=lambda x : x[1])

for name, _ in sorted_list:
    print(name)