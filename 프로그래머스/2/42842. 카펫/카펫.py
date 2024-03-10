import math

# yellow의 가로*2 + yellow의 세로*2 + 4 = brown

def solution(brown, yellow):
    area = brown + yellow
    answer = []
    for y in range(1, yellow + 1):
        if yellow % y == 0:
            y_col = y
            y_row = yellow/y
            if y_col * 2 + y_row * 2 + 4 == brown:
                answer.append(y_row + 2)
                answer.append(y_col + 2)
                break
    
    return answer