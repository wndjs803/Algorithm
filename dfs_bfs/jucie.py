# n - 행    m - 열
n, m = map(int, input().split())
data = []
for i in range(n):
    data.append(list(map(int,input())))

# 방문여부 확인하기 위한 리스트
visited = [[0]*m for _ in range(n)]

def dfs(x, y):
    # 틀의 범위를 벗어날 경우 함수 종료
    if x <0 or x>=n or y<0 or y>=m:
        return False
    # 칸막이가 존재하거나 이미 방문했을 경우 함수 종료
    if data[x][y] == 1 or visited[x][y] == 1:
        return False
    # 방문여부를 변경
    visited[x][y] = 1
    # 동, 남, 서, 북 순으로 순회
    dfs(x, y+1)
    dfs(x+1, y)
    dfs(x, y-1)
    dfs(x-1, y)
    
count = 0
# 반복문을 통해 틀의 모든 좌표를 순회
for i in range(n):
    for j in range(m):
        # 방문하지 않았을 때 dfs 실행
        if visited[i][j] != 1:
            # dfs가 실패하지 않았을 때 count 증가
            if dfs(i,j) != False:
                count +=1  

print(count)