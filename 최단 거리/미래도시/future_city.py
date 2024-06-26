# 이것이 코딩테스트다 with Python p259

INF = int(1e9)

n, m = map(int, input().split())

# 2차원 최소거리 저장 배열
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 선언
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

for i in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][i] + graph[i][b]) # 점화식을 통해 업데이트

result = graph[1][k] + graph[k][x]
if result >= INF:
    print(-1)
else: print(result)
