#w와 h의 최대공약수만큼 패턴 반복
#패턴 안의 안멀쩡한 사각형은 n+m-1

def gcd(x, y):
    if x < y:
        min = x
    else:
        min = y
    for i in range(min, 0, -1):
        if x%i == 0 and y%i == 0:
            gcd = i
            break
    return gcd

def solution(w,h):
    g = gcd(w, h)
    #return w * h - (g*((w//g)+(h//g)-1))
    return w * h - (w + h - g)

print(solution(8, 12))