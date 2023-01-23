from collections import deque

n, m, k, x = map(int, input().split())
# print(n,m,k,x)


path = [[] for _ in range(n+1)]

for i in range(m):
    road = list(map(int, input().split()))
    path[road[0]].append(road)

# print(path)

visited = [False for _ in range(n+1)]

queue = deque()
min_dis = [0 for _ in range(n+1)]
def bfs(start):
    queue.append(start)
    while queue:
        cur = queue.popleft()
        # print(cur)
        for i in path[cur]:
            queue.append(i[1])
            if visited[i[1]] == False:
                min_dis[i[1]] = min_dis[cur] +1
            visited[i[1]] = True
            # print(visited)
print(queue)
bfs(x)
# print(min_dis)
result = []
for i in range(len(min_dis)):
    if min_dis[i] == k:
        result.append(i)
        
        
if len(result) == 0:
    print(-1)
else:
    for j in result:
        print(j)

