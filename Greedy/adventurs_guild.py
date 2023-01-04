# n을 입력받는다.
n = int(input())
# 각 모험가의 공포도 입력 받고 오름차순으로 정렬한다.
fear = list(map(int, input().split()))
fear.sort()

count = 0

while True:
    #공포도가 가중 높은 것을 target으로 삼는다.
    target = fear[n-1]
    # 남은 사람이 0이거나 그 이하면 반복문 탈출
    if n <= 0:
        break
    # target만큼 사람이 같이 다녀야 하기 때문에 사람 수를 그만큼 뺸다.
    n = n - target
    # 그룹이 하나 늘었으므로 +1을 한다.
    count += 1

print(count)