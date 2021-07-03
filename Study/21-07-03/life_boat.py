# sorted 후 앞뒤로 인덱스를 움직인다

def solution(people, limit):
    answer = 0
    st = 0
    ed = len(people)-1

    people.sort()

    while st <= ed:
        if people[st]+people[ed] > limit:
            ed -= 1
        else:
            st += 1
            ed -= 1
        answer += 1

    return answer

print(solution([30,70,50,80,50], 100))