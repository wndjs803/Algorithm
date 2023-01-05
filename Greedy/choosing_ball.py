n, m = map(int, input().split())
data = list(map(int, input().split()))

choice = []
l = len(data)
for i in range(l):
    for j in range(i, l):
        if data[i] != data[j]: # 무게가 서로 같지 않으면 배열에 추가
            choice.append((i+1, j+1))
# 배열의 길이 출력
print(len(choice))