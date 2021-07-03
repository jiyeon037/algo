def solution(n):
    arr = [[0]*n for _ in range(n)]
    answer = []
    last = n*(n+1)/2

    x, y = 0, 0
    num = 1
    arr[x][y] = num
    dir = 0

    while num < last:
        if dir == 0:
            x += 1
            if x+1 >= n or arr[x+1][y] != 0:
                dir = 1

        elif dir == 1:
            y += 1
            if y+1 >= n or arr[x][y+1] != 0:
                dir = 2

        elif dir == 2:
            x -= 1
            y -= 1
            if y-1 <= 0 or x-1 <= 0 or arr[x-1][y-1] != 0:
                dir = 0

        num += 1
        arr[x][y] = num

    for i in range(n):
        for j in range(i+1):
            answer.append(arr[i][j])

    return answer

print(solution(4))