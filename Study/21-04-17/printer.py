from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque([(v, i) for i, v in enumerate(priorities)])

    while queue:
        print(max(queue))
        q = queue.popleft()
        if queue and max(queue)[0] > q[0]:
            queue.append(q)
        else:
            answer += 1
            if q[1] == location: # 순위가 같은 요소들이 있을 수 있으므로 요소의 index와 비교
                break

    return answer

priorities = [2,1,3,2]
location = 0
print(solution(priorities, location))