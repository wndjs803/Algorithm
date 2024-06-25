n =  int(input())

t_array = []
p_array = []

for _ in range(n):
    t, p = map(int, input().split())
    t_array.append(t)
    p_array.append(p)

dp = [0] * (n + 1)
max_value = 0

for i in range(n - 1, -1, -1):
    time = i + t_array[i]

    if time <= n:
        dp[i] = max(p_array[i] + dp[time], max_value)
        max_value = dp[i]
    else: dp[i] = max_value

print(max_value)