computer = int(input())
connect = int(input())

graph = [[] for _ in range(computer+1)]

for i in range(connect):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

visited = [False for _ in range(computer+1)]
count = 0
def dfs(cur):
    visited[cur] = True
    global count

    for next in graph[cur]:
        if not visited[next]:
            count += 1
            dfs(next)

dfs(1)
print(count)
