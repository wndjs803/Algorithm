def solution(sizes):
    big = []
    small = []
    
    for size in sizes:
        if size[0] > size[1]:
            big.append(size[0])
            small.append(size[1])
        else:
            big.append(size[1])
            small.append(size[0])
    
    result = max(big) * max(small)
    
    return result