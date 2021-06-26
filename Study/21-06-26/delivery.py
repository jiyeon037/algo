def solution(N, road, K):
    answer = 0
    INF = int(1e9)
    visited = [False] * (N+1)
    distance = [INF] * (N+1)
    graph = [[] for _ in range(N+1)]

    for i, j, cost in road:
        if cost > K:
            continue
        graph[i].append([j, cost])
        graph[j].append([i, cost])

    print(graph)

    def minimum_node():
        mini = INF
        index = 0
        for i in range(1, N+1):
            if distance[i] < mini and not visited[i]:
                mini = distance[i]
                index = i
        return index

    def dijkstra(start):
        distance[start] = 0
        visited[start] = True
        for g in graph[start]:
            print(graph[start])
            distance[int(g[0])] = int(g[1])
        
        for i in range(N-1):
            now = minimum_node()
            visited[now] = True
            for g in graph[now]:
                cost = distance[now] + g[1]
                if cost < distance[g[0]]:
                    distance[g[0]] = cost
        return distance
    
    dijkstra(1)

    for i in range(1, N+1):
        print(distance[i])
        if distance[i] <= K:
            answer += 1

    return answer

print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))