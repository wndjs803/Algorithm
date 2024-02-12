from collections import deque

def solution(prices):
    prices = deque(prices)
    answer = []
    count = 0
    
    while prices:
        price = prices.popleft()
        for i in prices:
            if price <= i:
                count += 1
            else:
                count += 1
                break
        answer.append(count)
        count = 0
            
    return answer
