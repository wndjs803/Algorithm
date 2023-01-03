#n, m 입력받기
n, m = map(int, input().split())
# 입력받은 값을 저장할 list 선언
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))
#최소값을 저장할 list 선언
min_num = []
for j in matrix:
    # 각 행마다 가장 작은 수를 append
    min_num.append(min(j)) #min(list) - list 중에 최소값 반환

# list 중 가장 큰 값을 출력    
print(max(min_num))