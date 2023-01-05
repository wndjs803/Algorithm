from itertools import combinations

n = int(input())
data = list(map(int, input().split()))
# 조합을 통해 모든 경우의 수를 구한다.
s = []
for i in range(1, n+1):
    s.extend(list(combinations(data, i)))
# 모든 경우의 수에 대한 합을 구한다
total = []
for j in s:
    total.append(sum(j))
# 중복을 없앤다.
total = list(set(total))

result = 0

if total[0] > 1: # 첫번째 값이 1보다 크다면 1원이 최솟값이다.
    result = 1
else:
    for k in range(len(total)-1): # 배열 순회
        if total[k+1] - total[k] != 1: # 다음 index의 값과 비교하여 1차이가 나지 않는다면
            result = total[k] +1 # 현재 index의 값에 1만 더해주면 된다.
            break # 반복문 탈출
        
if result == 0: # 만약에 1이상 차이 나는 구간이 없다면 제일 큰 값에 1을 더해준다..
    result = total[len(total)] +1

print(result)