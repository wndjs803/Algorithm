# Queue 활용을 위한 deque import
from collections import deque

n, m = map(int, input().split())
data = []
for i in range(n):
    data.append(list(map(int, input())))
# 방문 여부 확인 배열
visited = [[0]*m for _ in range(n)]
x, y = 0, 0
# 시작과 목표지점
start = [x, y]
end = [n-1, m-1]
# 경로 표시를 위한 배열
path = []
# bfs에서 활용하기 위한 배열
place = deque()
# 시작점을 미리 큐에 넣는다.
place.append(start)

def bfs(x, y):
    # 맵의 범위를 벗어나는지 확인
    if x<0 or y<0 or x>=n or y>=6:
        return False
    # 이미 방문했거나 괴물이 있는 지역인지 확인
    if visited[x][y] == 1 or data[x][y] == 0:
        return False
    # 몇 개이 후보를 추가했는지 확인하는 변수
    count = 0
    # 방문했으므로 1
    visited[x][y] = 1
    # 만약 목표지점에 도착했으면 True 반환
    if(end == [x, y]):
        return True
    # 동, 남, 서, 북 순으로 맵 범위 안에서 유효한 값일 경우 후보 추가
    if y+1 < m:
        if visited[x][y+1] == 0 and data[x][y+1] == 1:
            place.append([x, y+1])
            # 후보 개수 체크
            count += 1
    if x+1 < n:
        if visited[x+1][y] == 0 and data[x+1][y] == 1:
            place.append([x+1, y])
            count +=1
    if y-1>=0:
        if visited[x][y-1] == 0 and data[x][y-1] == 1:
            place.append([x, y-1])
            count += 1
    if x-1>=0:
        if visited[x-1][y] == 0 and data[x-1][y] == 1:
            place.append([x-1, y])
            count += 1
    # 만약 후보를 추가한 적이 없으면 다시 되돌아가야 함으로 path에서 제거한다.
    if count == 0:
        path.pop()

while True:
    # 큐 제일 앞에 있는 좌표를 현재 좌표로 지정
    cur = place.popleft()
    path.append(cur)
    x, y = cur[0], cur[1]
    # 현재 좌표로 bfs를 진행, True일 시 반복문 탈출
    if bfs(x,y) == True:
        break

# 경로의 길이를 출력
print(len(path))