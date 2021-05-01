from itertools import permutations

def is_prime(x):
    x = int(x)
    if x >= 2:
        for k in range(2, x):
            if x % k == 0:
                return False
        return True

def solution(numbers):
    answer = []
    nlist = []
    for n in numbers:
        nlist.append(n)

    for size in range(1, len(numbers)+1):
        plist = list(map(''.join, permutations(nlist,size)))
        plist = set(plist)

        for p in plist:
            p = int(p)
            if is_prime(p) == True:
                answer.append(p)
    
    answer = len(set(answer))

    return answer

print(solution("011"))