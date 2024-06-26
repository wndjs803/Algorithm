# 이것이 코딩테스다 with Python p.381
n = int(input())

ugly = [0] * n
ugly[0] = 1

i2 = i3 = i5 = 0 # 각각 2, 3, 5를 곱할 인덱스
next2, next3, next5 = 2, 3, 5 # 2, 3, 5를 곱한 값을 저장하는 변수(초기값은 1과 곱했다고 생각하면 될 듯 하다.)

for l in range(1, n):
    ugly[l] = min(next2, next3, next5) # 곱한 값 중 가장 작은 값을 할당

    if ugly[l] == next2: # 인덱스에 따라서 곱셈 결과를 증가
        i2 += 1 # 계속해서 인덱스를 증가 시킨다.(처음에는 ugly[0], 즉 1이었기 때문에 next2의 값은 2였다.)
        next2 = ugly[i2] * 2 # 그 다음 인덱스에 대해서도 2를 곱한다.(next2의 값은 4)
    if ugly[l] == next3:
        i3 += 1
        next3 = ugly[i3] * 3
    if ugly[l] == next5:
        i5 += 1
        next5 = ugly[i5] * 5

print(ugly[n - 1])

# 인덱스를 1씩 증가시키기에 각 인덱스의 값마다 2, 3, 5 각각을 모두 곱한 값을 빠짐없이 구할 수 있다.
