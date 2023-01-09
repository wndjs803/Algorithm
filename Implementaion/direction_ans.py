n = int(input())
x, y = 1, 1
plans = input().split()

# 명령어에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우는 무시
    if nx <1 or nx >n or ny<1 or ny>n:
        continue
    x, y = nx, ny
    
print(x, y)
            