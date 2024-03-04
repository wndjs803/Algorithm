from collections import defaultdict

def solution(clothes):
    clothes_type = defaultdict(int)
    
    for type in clothes:
        clothes_type[type[1]] += 1
    
    total = 1
    for num in clothes_type.values():
        total *= (num + 1)
    
    answer = total - 1
    return answer