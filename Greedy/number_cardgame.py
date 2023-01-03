n, m = map(int, input().split())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

min_num = []
for j in matrix:
    min_num.append(min(j)) #min(list) - list 중에 최소값 반환
    
print(max(min_num))