def solution(n):
    answer = ''

    while n>=1:
        
        tmp = n%3
        if tmp == 0:
            answer += '4'
            n -= 1
        else:
            answer += str(tmp)

        n //= 3

    answer = answer[::-1]
    return answer

print(solution(11))