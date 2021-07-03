from collections import deque

def solution(m, n, board):
    answer = 0

    for _ in range(m):
        poped = board.pop(0)
        board.append([p for p in poped])
    
    while True:
        counted = []
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == '0':
                    continue
                if board[i][j] == board[i][j+1]:
                    if board[i][j] == board[i+1][j] == board[i+1][j+1]:
                        counted.append((i,j))
                        counted.append((i,j+1))
                        counted.append((i+1,j))
                        counted.append((i+1,j+1))

        if not counted:
            break
        
        print(len(set(counted)))
        answer += len(set(counted))
        for c in counted:
            board[c[0]][c[1]] = '0'

        for i in range(m):
            for j in range(n):
                if board[i][j] == '0':
                    queue = deque()
                    for col in range(n):
                        for row in range(m-1, -1, -1):
                            if board[row][col] != '0':
                                queue.append(board[row][col])
                                board[row][col] = '0'

                        for row in range(m-1, -1, -1):
                            if queue:
                                board[row][col] = queue.popleft()

    return answer


board = ["AAA","AAA","AAA"]
#board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
#board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
print(solution(3,3,board))