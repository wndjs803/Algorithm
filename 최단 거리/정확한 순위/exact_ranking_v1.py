# 이것이 코딩테스다 with Python p.386

n, m = map(int, input().split())

INF = int(1e9)

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

for i in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][i] + graph[i][b])

count = [0] * (n + 1)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] != 0 and graph[i][j] != INF:
            count[i] += 1
            count[j] += 1

result = 0
for i in count:
    if i == (n - 1):
        result += 1
print(result)

# 플로이드 워셜 알고리즘 수행 이후 a로 올 수 있는 경로의 개수 + a에서 다른 곳으로 갈 수 있는 경로의 개수가
# n-1, 즉 자신을 제외한 수가 된다면 카운트 하도록 하였다.
