import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0
    while True:
        if scoville[0] < K:
            if len(scoville) >= 2:
                first = heapq.heappop(scoville)
                second = heapq.heappop(scoville)
                new_value = first + second*2
                heapq.heappush(scoville, new_value)
                count += 1
            else: return -1
        else: return count
    
    return count