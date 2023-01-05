n, m = map(int, input().split())
data = list(map(int, input().split()))
# 1부터 10까지의 무게를 담을 리스트
array = [0] * 11
# 각 무게에 대한 공의 개수
for x in data:
    array[x] += 1
    
result = 0

for i in array:
    n -= array[i] # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
    result += (array[i] * n) # B가 선택하는 경우의 수와 곱하기

print(result)