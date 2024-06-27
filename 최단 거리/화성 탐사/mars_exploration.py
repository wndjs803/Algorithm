import heapq

INF = int(1e9)

t = int(input())

dx = [1, 0, -1, 0]
dy = [0, 1, 0 ,-1]

for _ in range(t):
    n = int(input())
    graph = []

    for _ in range(n):
        graph.append(list(map(int, input().split())))
    
    start = (0, 0)
    goal = (n - 1, n - 1)
    distance = [[INF] * n for _ in range(n)]

    q = []
    heapq.heappush(q, (graph[0][0], start))
    distance[0][0] = graph[0][0]

    while q:
        dist, now = heapq.heappop(q)
        x, y = now[0], now[1]
        if distance[x][y] < dist:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            
            cost = dist + graph[nx][ny]
            if cost < distance[nx][ny]:
                heapq.heappush(q, (cost, (nx, ny)))
                distance[nx][ny] = cost

        if distance[n -1][n -1] != INF:
            print(distance[n -1][n -1])
            break
