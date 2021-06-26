def solution(clothes):
    dic = dict()
    for i in clothes:
        if i[1] in dic:
            dic[i[1]] += 1
        else:
            dic[i[1]] = 2 # 안입는 경우를 미리 추가해줌
        
    answer = 1
    for i in dic:
        answer *= dic[i]
    return answer-1

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))