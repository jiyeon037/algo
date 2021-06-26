from itertools import combinations, filterfalse

def solution(relation):
    answer = 0
    all = []
    unique = []

    if len(relation) > 0:
        col_size = len(relation[0])
        row_size = len(relation)

    for i in range(1, col_size + 1):
        all.extend([k for k in combinations([j for j in range(col_size)],i)])

    for comb in all:
        vaild_set = set()
        for row in range(row_size):
            temp = ''
            for col in comb:
                temp += relation[row][col]

    print(all)
    return

relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
print(solution(relation))