import copy

def rotate(key):
    M = len(key)
    ret = [[0] * M for _ in range(M)]

    for i in range(M):
        for j in range(M):
            ret[j][M-1-i] = key[i][j]
    return ret

def solution(key, lock):
    N = len(lock)
    M = len(key)
    paddingN = N + (M-1) * 2

    for _ in range(0, 4):
        rotated_key = rotate(key)
        key = copy.deepcopy(rotated_key)

        for i in range(N+M-1):
            for j in range(N+M-1):
                biglock = [[0] * paddingN for _ in range(paddingN)]

                # biglock 초기화
                for r in range(N):
                    for c in range(N):
                        biglock[r+M-1][c+M-1] = lock[r][c]

                for r in range(M):
                    for c in range(M):
                        biglock[r+i][c+j] += rotated_key[r][c]

                cnt = 0
                for r in range(M-1, M+N-1):
                    for c in range(M-1, M+N-1):
                        if biglock[r][c] == 1:
                            cnt += 1
                
                if cnt == N*N:
                    return True

    return False
                        

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))