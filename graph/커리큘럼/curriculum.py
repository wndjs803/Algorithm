# 이것이 코딩테스다 with Python p.303

from collections import deque
import copy

n = int(input())

graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
costs = [0] * (n + 1)

for i in range(1, n + 1):
    array = list(map(int, input().split()))
    for j in range(len(array)):
        if array[j] == -1: break

        if j == 0:
            costs[i] = array[j]
        else:
            graph[array[j]].append(i)
            indegree[i] += 1

q = deque()

for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)

result = copy.deepcopy(costs) # 초기 비용을 모두 복사

while q:
    now = q.popleft()

    for i in graph[now]:
        indegree[i] -= 1
        result[i] = max(result[i], (result[now] + costs[i])) # 인접해있는 i의 현재 비용, (현재 노드의 비용 + i의 초기 비용) 둘 중 큰 거

        if indegree[i] == 0:
            q.append(i)

for i in range(1, n + 1):
    print(result[i])
