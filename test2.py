#from itertools import combinations
from collections import defaultdict


def combinations(iterable, r):
    pool = "".join(sorted(iterable))
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield "".join(sorted(pool[i] for i in indices))
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield "".join(sorted(pool[i] for i in indices))


def solution(orders, course):
    answer = []
    for n in course:
        count_dict = defaultdict(int)
        for order in orders:
            combos = list(combinations(order, n))
            for combo in combos:
                count_dict[combo] += 1
        max_count = 2
        local_result = []
        for combo, count in count_dict.items():
            if count > max_count:
                local_result = [combo]
                max_count = count
            elif count == max_count:
                local_result.append(combo)

        answer.extend(local_result)
                
    return sorted(answer)


a = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
b = [2,3,4]
print(solution(a, b))