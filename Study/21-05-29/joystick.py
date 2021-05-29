def solution(name):
    answer = 0
    name = list(name)
    idx = 0

    while True:
        right = 1
        left = 1
        if name[idx] != 'A':
            if 'A' <= name[idx] <= 'M':
                answer += ord(name[idx]) - 65
            else:
                answer += 90 - ord(name[idx]) + 1
            name[idx] = 'A'

        if name == ['A'] * len(name):
            break
        
        for i in range(1, len(name)):
            if name[idx+i] == 'A':
                right += 1
            else:
                break
        for i in range(1, len(name)):
            if name[idx-i] == 'A':
                left += 1
            else:
                break

        if right > left:
            answer += left
            idx -= left
        else:
            answer += right
            idx += right

    return answer

print(solution("BBBAAAAABBB"))