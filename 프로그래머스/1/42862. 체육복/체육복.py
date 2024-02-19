def solution(n, lost, reserve):
    _lost = [x for x in lost if x not in reserve]
    _reserve = [x for x in reserve if x not in lost]
    _lost.sort()
    _reserve.sort()
    for num in _reserve:
        minus = num - 1
        flus = num + 1
        if minus in _lost:
            _lost.remove(minus)
        elif flus in _lost:
            _lost.remove(flus)
    
    answer = n - len(_lost)
    return answer