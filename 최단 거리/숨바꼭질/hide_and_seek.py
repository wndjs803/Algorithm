# 이것이 코딩테스트다 with Python p.390
INF = int(1e9)

n, m = map(int, input().split())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for i in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][i] + graph[i][b])

dist = max(graph[1][1:])
num = graph[1].index(dist)

count = 0
for i in range(1, n + 1):
    if dist == graph[1][i]:
        count += 1

print(num, dist, count)
