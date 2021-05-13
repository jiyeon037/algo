import heapq

#섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
def solution(scoville, k):
    heapq.heapify(scoville)

    cnt = 0
    while scoville[0] < k:
        if len(scoville) > 1:
            heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville) * 2)
            cnt += 1
        else:
            return -1
    return cnt


print(solution([2,1,3,9,10,12], 7))