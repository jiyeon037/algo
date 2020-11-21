from itertools import combinations

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
members = [i for i in range(N)]

# 가능한 팀의 조합
teams = list(combinations(members, N//2))
len_teams = len(teams)
answer = 999

for i in range(len_teams//2):
    start_sum = 0
    for j in range(N//2):
        member = teams[i][j]
        for k in teams[i]:
            start_sum += S[member][k]
    
    link_sum = 0
    for j in range(N//2):
        member = teams[-i-1][j]
        for k in teams[-i-1]:
            link_sum += S[member][k]

    answer = min(answer, abs(start_sum - link_sum))

print(answer)