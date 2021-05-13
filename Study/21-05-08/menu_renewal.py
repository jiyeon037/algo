from itertools import combinations
from collections import Counter

orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]

def solution(orders, course):
    answer = []

    for i in course:
        combi_list = []
        for order in orders:
            for j in combinations(order, i):
                combi_list.append(''.join(sorted(j)))
        print(combi_list)

        if not combi_list:
            continue
        
        combi_list = Counter(combi_list).most_common()
        word, cnt = combi_list[0]
        for w, c in combi_list:
            if c > 1 and cnt == c:
                answer.append(w)

    return sorted(answer)

print(solution(orders, course))