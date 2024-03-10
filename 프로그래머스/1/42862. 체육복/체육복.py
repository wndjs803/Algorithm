def solution(n, lost, reserve):
    new_lost = [l for l in lost if l not in reserve]
    new_reserve = [r for r in reserve if r not in lost]
    
    new_lost.sort()
    new_reserve.sort()
    
    for value in new_reserve:
        if value - 1 in new_lost:
            new_lost.remove(value - 1)
            continue
        if value + 1 in new_lost:
            new_lost.remove(value + 1)
            continue
            
    return n - len(new_lost)