from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque()

    if cacheSize == 0:
        return len(cities) * 5

    i = 0
    for city in cities:
        city = city.lower()
        if city in cache:
            answer += 1
            cache.remove(city)
            cache.append(city)
        else:
            answer += 5
            if i < cacheSize:
                cache.append(city)
                i += 1
            else:
                cache.popleft()
                cache.append(city)

    return answer


print(solution(4, ["C","B","A","A"]))
#print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))
#print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"])) # 21
#print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
