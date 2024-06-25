# 이것이 코딩테스트다 with Python p.375
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    # d[i][j] = max(d[i][j-1], d[i+1][j-1], d[i-1][j-1])
    d =[[0 for _ in range(m + 1)] for _ in range(n + 2)]
    index = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            d[i][j] = array[index]
            index += 1
    
    for i in range(2, m + 1):
        for j in range(1, n + 1):
            max_value = max(d[j][i-1], d[j+1][i-1], d[j-1][i-1])
            d[j][i] = d[j][i] + max_value
    
    result = -1
    for i in range(1, n + 1):
        result = max(result, d[i][m])

    print(result)
            
