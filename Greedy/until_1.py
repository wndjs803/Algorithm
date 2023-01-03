n, k = map(int, input().split())

count = 0
# n이 1이 아닐 동안 반복
while n!=1:
    # n이 k로 나누어지지 않으면 -1
    if n%k != 0:
        n -= 1
        # count는 항상 한다.
        count += 1
    else:
        n = n/k
        count += 1

print(count)