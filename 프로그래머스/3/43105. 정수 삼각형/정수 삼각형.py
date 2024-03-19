def solution(triangle):
    dp = []
    dp.append(triangle[0])
    
    for i in range(1, len(triangle)):
        total = []
        for j in range(len(triangle[i])):
            if j == 0:
                num = dp[i-1][0] + triangle[i][0]
                total.append(num)
            elif j < len(triangle[i-1]):
                num1 = dp[i-1][j-1] + triangle[i][j]
                num2 = dp[i-1][j] + triangle[i][j]
                total.append(max(num1, num2))
            else:
                num = dp[i-1][j-1] + triangle[i][j]
                total.append(num)
        
        dp.append(total)
        
    answer = max(dp[-1])
                
    return answer