# yellow를 1~yellow까지 돌면서 약수를 찾는다
# 약수를 찾으면, (1번 식과) 2번 식을 만족하면 리턴

# x * y = yellow
# yellow = 12


def solution(brown, yellow):
    answer = []
    for i in range(1, (yellow+1)):
        if yellow % i == 0:
            if 2*(i+(yellow//i))+4 == brown:
                answer.append((yellow//i)+2)
                answer.append(i+2)
                return answer

print(solution(10,2))