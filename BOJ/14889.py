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
    link_sum = 0
    start_team = teams[i]
    link_team = teams[-i-1]

    for j in range(N//2):
        start_member = start_team[j]
        link_member = link_team[j]

        for k in start_team:
            start_sum += S[start_member][k]
    
        for k in link_team:
            link_sum += S[link_member][k]

    answer = min(answer, abs(start_sum - link_sum))

print(answer)