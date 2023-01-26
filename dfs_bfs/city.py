# 큐를 활용하기 위해 deque import
from collections import deque

n, m, k, x = map(int, input().split())
# 각 도시의 경로를 저장할 배열
path = [[] for _ in range(n+1)]
# 인접 리스트 형식으로 경로 입력 받기
for i in range(m):
    road = list(map(int, input().split()))
    path[road[0]].append(road[1])

queue = deque()
# 최단 거리 저장할 배열 선언
min_dis = [0 for _ in range(n+1)]
def bfs(start):
    # 시작점을 큐에 넣고 시작
    queue.append(start)
    while queue:
        cur = queue.popleft()
        for i in path[cur]: # 현재 도시에서 갈 수 있는 도시 순회
            if min_dis[i] == 0: # 방문을 하지 않은 도시라면
                min_dis[i] = min_dis[cur] +1 # 현재 도시보다 거리+1
                queue.append(i) # 큐에 다음 도시 넣기

bfs(x)

# 만족한 값 존재 여부에 대한 변수
empty = True
for i in range(len(min_dis)):
    if min_dis[i] == k: # 특정 거리의 값이 있다면 출력
        print(i)
        empty = False 
        
if empty:
    print(-1)

