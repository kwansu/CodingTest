from collections import defaultdict

INF = 2147483647

def solution(sales, links):
    cache = [[INF, INF] for _ in range(len(sales) + 1)]
    teams = defaultdict(list)
    for k, v in links:
        teams[k].append(v)

    def calc_min_cost(n):
        cost = 0
        if n in teams:
            exist = False
            for m in teams[n]:
                i = calc_min_cost(m)
                if i:
                    exist = False
                cost += cache[m][i]

            if exist:
                cache[n][0] = cost
            else:
                min_diff = INF
                for m in teams[n]:
                    min_diff = min(min_diff, cache[m][1] - cache[m][0])
                cache[n][0] = cost + min_diff
        else:
            cache[n][0] = 0
        cache[n][1] = cost + sales[n-1]

        return 1 if cache[n][0] >= cache[n][1] else 0

    calc_min_cost(1)
    return min(cache[1][0], cache[1][1])


a = solution(
    [14, 17, 15, 18, 19, 14, 13, 16, 28, 17],
    [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]],
)
print(a)
print(a == 44)
