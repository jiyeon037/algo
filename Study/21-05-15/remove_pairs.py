def solution(s):
    answer = 0
    stack = []

    for c in s:
        if len(stack) >= 1:
            if stack[-1] == c:
                stack.pop()
                continue
        stack.append(c)
    
    if not stack:
        answer = 1
    else:
        answer = 0

    return answer

print(solution("baabaa"))