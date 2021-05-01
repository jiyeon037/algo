def divide(w):
    cnt = 0
    for i in range(len(w)):
        if w[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            return w[:i+1], w[i+1:]

def is_correct(u):
    stack = []
    for s in u:
        if s == '(':
            stack.append(s)
        else:
            if not stack:
                return False
            stack.pop()
    return True

def solution(w):
    answer = ''
    # 1번
    if w == '':
        return ''
    # 2번
    u, v = divide(w)
    # 3번
    if is_correct(u):
        return u + solution(v)
    #4번
    else:
        answer += '('
        answer += solution(v)
        answer += ')'

        for s in u[1:len(u)-1]:
            if s == '(':
                answer += ')'
            else:
                answer += '('

        return answer
            
print(solution("()))((()"))