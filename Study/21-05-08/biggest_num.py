def solution(numbers):
    nlist = []
    for n in numbers:
        nlist.append(str(n))
    nlist = sorted(nlist, key=lambda x : x*3, reverse = True)
    return str(int(''.join(nlist)))

print(solution([0,0,0,0,0]))