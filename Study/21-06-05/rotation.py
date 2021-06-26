def solution(rows, columns, queries):
    answer = []
    arr = [[0 for _ in range(columns)] for _ in range(rows)]
    
    t = 1
    for i in range(rows):
        for j in range(columns):
            arr[i][j] = t
            t += 1

    print(arr)

    return answer

print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))