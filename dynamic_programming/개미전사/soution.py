# 이것이 코딩테스트다 with Python p.220

n = int(input())
array = list(map(int, input().split()))

d = [0] * n

# d[i] = max(d[i-1], d[i-2]+k)

d[0] = array[0]
d[1] = max(array[0], array[1])

for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + array[i])

print(d[n-1])
