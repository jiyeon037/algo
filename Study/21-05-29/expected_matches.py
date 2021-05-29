def recursive(a,b,cnt):
    if a == b:
        return cnt
    return recursive((a+1)//2, (b+1)//2, cnt + 1)

def solution(n,a,b):
    return recursive(a,b,0)

print(solution(16, 10, 13))