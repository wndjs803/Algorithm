n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0
count  = 0

for i in data:
    # 현재 그룹에 해당 모험가 포함시키기
    count += 1
    # 만약 현재 모험가 수가 현재 공포도 i 이상이라면 그룹을 결성
    if count >= i:
        result += 1
        count = 0
        
print(result)