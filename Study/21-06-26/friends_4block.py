def solution(m, n, board):
    answer = 0

    for _ in range(m):
        poped = board.pop(0)
        board.append([p for p in poped])
    
    while True:
        counted = []
        flag = False
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == board[i][j+1]:
                    if board[i][j] == board[i+1][j] == board[i+1][j+1] != '0':
                        flag = True
                        counted.append((i,j))
                        counted.append((i,j+1))
                        counted.append((i+1,j))
                        counted.append((i+1,j+1))

        if flag == False:
            break

        answer += len(set(counted))
        for c in counted:
            board[c[0]][c[1]] = '0'

        for i in range(m):
            for j in range(n):
                if board[i][j] == '0':

                    for row in range(m-1, -1, -1):
                        for col in range(n):
                            if board[row][col] == '0':
                                for k in range(row-1,-1,-1):
                                    if board[k][col] != '0':
                                        tmp = board[k][col]
                                        board[k][col] = board[row][col]
                                        board[row][col] = tmp
                                        break
    return answer



board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
#board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
print(solution(4,5,board))