'''
def solution(citations):
    for h_candidate in range(max(citations), -1, -1):
        h_up = 0
        for c in citations:
            if c >= h_candidate:
                h_up += 1
            if h_up >= h_candidate:
                return h_candidate
'''
def solution(citations):
    h_index = -1
    for h_candidate in range(0, max(citations)+1):
        h_up = 0
        for c in citations:
            if c >= h_candidate:
                h_up += 1
            if h_up >= h_candidate:
                h_index = max(h_index, h_candidate)
    return h_index

print(solution([6,0,3,1,5]))