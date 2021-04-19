import math

def solution(progresses, speeds):
    answer = []
    days = []
    stack = []
    popCnt = 0
    maxStack = -1

    size = len(progresses)

    # 1. 배포 일수를 list로 구하기
    for i in range(size):
        days.append(math.ceil((100 - progresses[i]) / speeds[i]))

    print(days)

    # 2.해당 list로 스택 작업
    for d in days:
        if not stack:
            stack.append(d)
            maxStack = d
        else:
            if d > maxStack:
                maxStack = d
                while stack:
                    stack.pop()
                    popCnt += 1
                answer.append(popCnt)
                popCnt = 0
            
            stack.append(d)
        
    if stack:
        while stack:
            stack.pop()
            popCnt += 1
        answer.append(popCnt)
    
    return answer

progresses = [40, 93, 30, 55, 60, 65]
speeds = [60, 1, 30, 5, 10, 7]

print(solution(progresses, speeds))