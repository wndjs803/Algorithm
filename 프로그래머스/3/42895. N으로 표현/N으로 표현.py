def solution(N, number):
    dp = []
    
    # count - N을 사용한 횟수
    for count in range(1, 9): # 최솟값 8
        combination = set()
        combination.add(int(str(N)*count))
        
        for i in range(count-1):
            for l in dp[i]:
                for r in dp[-i -1]:
                    combination.add(l + r)
                    combination.add(l - r)
                    combination.add(l * r)
                    if r != 0:
                        combination.add(l / r)
            
        if number in combination:
            return count
        
        dp.append(combination)
        
    return -1