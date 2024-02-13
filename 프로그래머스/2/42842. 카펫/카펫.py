import math

def solution(brown, yellow):
    area = brown + yellow
    half = math.ceil(brown/2.0)
    answer = []
    row = 0
    col = 0
    for i in range(half, 0, -1):
        if area%i == 0:
            if (i*2 + area/i*2) == brown + 4:
                answer.append(i)
                answer.append(area/i)
                break
    
    return answer