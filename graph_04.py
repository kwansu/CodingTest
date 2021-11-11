N = 5

inputs = [None]
inputs.append((10,))
inputs.append((10, 1))
inputs.append((4, 1))
inputs.append((4, 3, 1))
inputs.append((3, 3))


times = [None] * (N+1)
def find_time(n):
    if times[n] == None:
        max_time = 0
        time, *edge = inputs[n]
        for pre_n in edge:
            max_time = max(max_time, find_time(pre_n))
        times[n] = max_time + time
    return times[n]


for n in range(N):
    print(find_time(n+1))
    