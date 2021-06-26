def solution(s):
    answer = 0
    def check(s):
        dic = {'(':')', '{':'}', '[':']'}
        stack = []
        for i in range(len(s)):
            if s[i] in "({[":
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                elif s[i] == dic[stack[-1]]:
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else :
            return False
        
    for i in range(len(s)):
        new_s = s[i:]+s[:i]
        if check(new_s):
            answer += 1    
    return answer

s = "}]()[{"
print(solution(s))