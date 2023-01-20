n= 5
data = [[2]*n for _ in range(n)]
build_frame = [[1,0,0,1],
               [1,1,1,1],
               [2,1,0,1],
               [2,2,1,1],
               [5,0,0,1],
               [4,2,1,1],
               [3,2,1,1]]
# x, y: 좌표 a: 0-기둥 1-보  b:0-삭제 1-설치
# 1. 좌표 확인
# 2. 구조물 확인
# 3. 설치여부 확인
# 4. 설치 or 삭제 실시
def check_pi(x, y):
    if data[y][x] == 1 or data[y][x] == 0 or y==0:
        return True
    else:
        return False
    
def check_pd(x, y):
    if data[y][x-1] == 1 or data[y][x+1] == 1:
        return True
    else:
        return False

def check_bi(x, y):
    if data[y][x] == 1 or data[y][x+1] == 1 or (data[y][x] == 0 and data[y][x+1] == 0):
        return True
    else:
        return False  
    
def check_bd(x, y):
    if data[y-1][x-1] == 1 or data[y-1][x+1] == 1:
        return True
    else:
        return False  

def installing(x, y, some, install):
    if some == 0:
        if install == 1:
            if check_pi(x, y):
                data[y][x] == 1
                data[y+1][x] == 1
        else:
            if check_pd(x, y):
                data[y][x] == 2
                data[y+1][x] == 2
    else:
        if install == 1:
            if check_bi(x, y):
                data[y][x] == 0
                data[y][x+1] == 0
        else:
            if check_bd(x, y):
                data[y][x] == 2
                data[y][x+2] == 2

for i in build_frame:
    x = i[0]
    y = i[1]
    some = i[2]
    install = i[3]
    installing(x, y, some, install)

# for i in range(len(data)):
#     for j in range(len(data)):
#         if data[i][j]
print(data)