from collections import deque

n, m , v = map(int, input().split())

graph = [[] for _ in range(n+1)]


for i in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

for i in range(1, n+1):
    graph[i].sort()

visited = [False for _ in range(n+1)]

def dfs(cur):
    visited[cur] = True
    print(cur, end=" ")

    for next in graph[cur]:
        if visited[next] == False:
            dfs(next)

dfs(v)
print()
visited = [False for _ in range(n+1)]

def bfs(v):
    queue = deque()
    queue.append(v)

    while queue:
        cur = queue.popleft()
        visited[cur] = True
        print(cur, end=" ")

        for next in graph[cur]:
            if visited[next] == False:
                visited[next] = True
                queue.append(next)

bfs(v)