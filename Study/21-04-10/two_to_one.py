arr = [0,0]
sumarr = []

def func(cur_depth, prev_idx, isused, numbers):
    if cur_depth == 2:
        sumarr.append(arr[0] + arr[1])
        return

    for i in range(len(numbers)):
        if isused[i] == True or prev_idx > i:
            continue
        isused[i] = True
        arr[cur_depth] = numbers[i]
        func(cur_depth+1, i, isused, numbers)
        isused[i] = False


def solution(numbers):
    isused = [False] * len(numbers)
    #numbers.sort()
    func(0, 0, isused, numbers)

    print(sumarr)
    answer = sorted(list(set(sumarr)))

    return answer

numbers = [2,1,3,4,1]
print(solution(numbers))