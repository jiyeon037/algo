def solution(s):
    answer = []
    s = s[2:-2].split("},{")
    s = sorted(s, key=len)

    for i in s:
        ii = i.split(",")
        for j in ii:
            if int(j) not in answer:
                answer.append(int(j))

    return answer

print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))