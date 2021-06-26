from itertools import combinations
from bisect import bisect_left

# 1. 문자열 전처리
# 2. key-value 해쉬(딕셔너리)
# 3. 조합, 이진 탐색

def solution(info, query):
    return

'''
def solution(info, query):
    answer = []
    for que in query:
        q = que.split()
        cnt = 0
        for inf in info:
            i = inf.split()
            if q[0] != "-":
                if q[0] != i[0]:
                    continue
            if q[2] != "-":
                if q[2] != i[1]:
                    continue
            if q[4] != "-":
                if q[4] != i[2]:
                    continue
            if q[6] != "-":
                if q[6] != i[3]:
                    continue
            if int(i[4]) >= int(q[7]):
                cnt += 1
        answer.append(cnt)
    return answer
'''

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

print(solution(info, query))