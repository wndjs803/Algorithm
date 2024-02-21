def rank(num):
    if num == 6:
        return 1
    if num == 5:
        return 2
    if num == 4:
        return 3
    if num == 3:
        return 4
    if num == 2:
        return 5
    
    return 6

def solution(lottos, win_nums):
    answer = []
    correct = 0
    zero = 0
    for num in lottos:
        if num in win_nums:
            correct += 1
        elif num == 0:
            zero += 1
    
    max_point = correct + zero
    
    answer.append(rank(max_point))
    answer.append(rank(correct))
    
    return answer
