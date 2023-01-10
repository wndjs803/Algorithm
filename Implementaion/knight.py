pos = input()
#(수평 수직) 움직일 수 있는 모든 경우의 수
move = [[1, 2], [1, -2], [-1, 2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]]

x_a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

row = x_a.index(pos[0]) # index를 활용해 좌표 찾기
col = int(pos[1]) - 1

count =0

for i in move:
    dx = row + i[0]
    dy = col + i[1]
    #범위 체크
    if dx > 7 or dx < 0 or dy > 7 or dy < 0:
        continue
    else:
        count +=1
        
print(count)
