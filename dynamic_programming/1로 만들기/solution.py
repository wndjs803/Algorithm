# 이것이 코딩테스트다 with python

x = int(input())

d = [0] * 30001

for i in range(2, x+1):
    # 현재 수에서 1을 뺴는 경우
    d[i] = d[i-1] + 1 # i-1 이라는 숫자가 호출이 되었다는 의미

    # 현재 수가 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1) # 기존 호출 횟수(d[i])와 2로 나누어떨어졌을 때의 수(d[i // 2] + 1)에 대한 호출 중 작은 것을 선택
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)

    # 여기서 elif가 아닌 이유도 모든 경우의 수를 따져서 최소를 고르기 위함

print(d[x])
