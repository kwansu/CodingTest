N = int(input())
assert(1 <= N <= 1000)

memory = [0]*N
memory[0] = 1
memory[1] = 3

if N >= 3:
    for n in range(2, N):
        memory[n] = memory[n-1] + memory[n-2] * 2

print(memory[N-1])