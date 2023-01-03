n, k = map(int, input().split())
result = 0

while True:
    # n // k 로 몫을 구한 다음 k를 곱하면 k로 나누어지는 최댓값을 구할 수 있다.
    target = (n //k) * k
    # n - target 은 -1을 몇 번할지 말해준다.
    result += (n-target)
    n = target
    # n이 k보다 작으면 k로 나눌 수 없으므로 반복문을 탈출한다.
    if n < k:
        break
    # n은 지금 k로 나누어 떨어지는 상태이므로 나눌 때마다 +1을한다.
    result += 1
    n //= k
# n=1이어야 하기 때문에 n-1 만큼 -1을 해줘야 한다.
result += (n-1)
print(result)