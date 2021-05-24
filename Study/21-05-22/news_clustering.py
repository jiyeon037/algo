from collections import Counter
# J(A,B) = 교집합 크기 / 합집합 크기

str1 = "FRANCE"
str2 = "french"

#1) 소 -> 대 변환
#2) 2개씩 쪼개 집합 만들기
#3) 교집합, 합집합 만들기

def solution(str1, str2):
    answer = 0
    set1 = []
    set2 = []
    intersections = 0
    unions = 0

    str1 = str1.upper()
    str2 = str2.upper()

    for i in range(len(str1)-1):
        if str1[i:i+2].isalpha():
            set1.append(str1[i:i+2])
    
    for i in range(len(str2)-1):
        if str2[i:i+2].isalpha():
            set2.append(str2[i:i+2])

    inter = (set1) & (set2)
    print(inter)

    set1 = Counter(set1)
    set2 = Counter(set2)

    intersections = set1 & set2
    unions = set1 | set2

    u_num = sum(list(unions.values()))
    i_num = sum(list(intersections.values()))

    print(u_num, " ", i_num)

    if u_num == 0:
        answer = 1
    else:
        answer = i_num / u_num
    return int(answer * 65536)

print(solution(str1,str2))