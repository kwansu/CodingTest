from bisect import bisect_left

def solution(info, query):
    answer = []
    idx_map = {"-": 0, 
               "cpp": 27, "java": 54, "python": 81,
               "backend": 9, "frontend": 18,
               "junior": 3, "senior": 6,
               "chicken": 1, "pizza": 2}
    
    groups = [[] for _ in range(4*3*3*3)]
    for x in info:
        data = x.split()
        score = int(data[-1])
        indices = [idx_map[data[i]] for i in range(4)]
        for i in range(16):
            idx = 0
            for j in range(4):
                if i & 1<<j:
                    idx += indices[j]
            groups[idx].append(score)

    groups = [sorted(group) for group in groups]
    
    for x in query:
        data, score = x.rsplit(maxsplit=1)
        score = int(score)
        data = data.split(" and ")
        idx = 0
        for i in data:
            idx += idx_map[i]
        
        group = groups[idx]
        a = len(group) - bisect_left(group, score)
        answer.append(a)

    return answer


a = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
b = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(a, b))