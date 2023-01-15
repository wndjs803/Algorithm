# 맵 크기 입력
size = list(map(int, input().split()))
# 유저의 좌표와 방향
row, col, direction = map(int, input().split())
#바다 육지 입력
world = []
for i in range(size[0]):
    world.append(list(map(int, input().split())))
# 행이동 열이동 저장    
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
# 방문한 곳 저장
place = []
place.append([row, col])
# 바다를 맞다뜨린 횟수
count = 0

while True:
    # 90도 회전
    direction -= 1
    if direction < 0:
        direction += 4
    # 새로운 위치 탐색
    new_row = row + dr[direction]
    new_col = col + dc[direction]
    # 새로운 위치가 육지(0)이고 가보지 않았던 곳이면 위치 이동
    if world[new_row][new_col] == 0 and [new_row, new_col] not in place:
        row = new_row
        col = new_col
        place.append([new_row, new_col]) # 가본 곳 체크
        count = 0
        continue
    else:
        count += 1
        print("count : "+ str(count))
    
    if(count >= 4): # 네방향 모두 갈 수 없을 떄
        direction -= 2 # 뒤 방향 탐색
        if direction < 0:
            direction += 4
        new_row = row + dr[direction]
        new_col = col + dc[direction]
        if world[new_row][new_col] == 0:
            row = new_row
            col = new_col
        else: # 뒤도 바다일 경우 반복문 탈출
            break

print(len(place))