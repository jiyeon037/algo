record = ["Enter uid1234 김지연", "Enter uid4567 노수일", "Change uid4567 김지연", "Change uid1234 무지", "Leave uid1234"]

def solution(record):
    dic = {}
    answer = []
    for r in record:
        data = r.split()
        # 고유번호의 닉네임을 저장한다
        if data[0] == 'Enter' or data[0] == 'Change':
            dic[data[1]] = data[2]

    for r in record:
        data = r.split()
        if data[0] == 'Enter':
            answer.append(dic[data[1]]+"님이 들어왔습니다.")
        elif data[0] == 'Leave':
            answer.append(dic[data[1]]+"님이 나갔습니다.")
    return answer

print(solution(record))