import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드, 간선 개수
n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n + 1)]
# 최소 거리를 저장하는 배열
distance = [INF] * (n + 1)

for _ in range(m):
    # a -> b 로 가는 비용은 c이다
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    # 거리, 노드
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist: # 현재 노드의 최소거리가 큐에 저장되어있던 거리보다 작으면 진행할 필요없다
            continue

        for i in graph[now]: # 현재(now)랑 연결된 노드 순회
            cost = dist + i[1] # 현재 거리 + i 노드의 거리
            if cost < distance[i[0]]: # cost가 기존의 distance(최소 거리)보다 작으면 
                distance[i[0]] = cost # distance 갱신
                heapq.heappush(q, (cost, i[0])) # 큐에 저장

dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INF")
    else: print(distance[i])
