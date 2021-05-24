from itertools import permutations
from collections import deque

def operation(a,b,x):
    if x=='+':
        return a+b
    elif x=='-':
        return a-b
    else:
        return a*b

def calculation(op, exp):
    for i in op:
        now_op = i

        new_exp = deque() # []
        while exp:
            now = exp.popleft()

            if now == now_op:
                a = new_exp.pop()
                b = exp.popleft()
                c = operation(int(a), int(b), now_op)
                new_exp.append(c)
            else:
                new_exp.append(now)        
        exp = new_exp

    return abs(int(exp.popleft()))


def solution(expression):
    answer = 0

    num = ''
    exp = deque()
    for i in expression:
        if i.isdigit():
            num += i
        else:
            exp.append(num)
            exp.append(i)
            num = ''
    exp.append(num)

    print(exp)

    operators = ['+', '-', '*']

    for op in permutations(operators, 3):
        copy_exp = exp.copy()
        result = calculation(op, copy_exp)

        if answer < result:
            answer = result
    return answer

print(solution("100-200*300-500+20"))