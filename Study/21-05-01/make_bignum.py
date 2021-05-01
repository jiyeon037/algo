from itertools import combinations

def solution(number, k):
    answer = []

    for i,num in enumerate(number):

        while len(answer) > 0 and num > answer[-1] and k > 0:
            k -= 1
            answer.pop()
        
        if k == 0:
            answer += number[i:]
            break

        answer.append(num)

    answer = answer[:-k] if k > 0 else answer
    return ''.join(answer)

''' 모든 경우의 수 조합 접근 시간초과
def solution(number, k):
    clist = []
    k = len(number)-k
    for n in number:
        clist.append(n)

    clist = list(map(''.join, combinations(clist, k)))
    answer = max(clist)

    return answer
'''

print(solution("9876543", 4))