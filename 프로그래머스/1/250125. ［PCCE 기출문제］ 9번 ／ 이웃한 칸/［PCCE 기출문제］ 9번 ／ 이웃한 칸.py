def solution(board, h, w):
    answer = 0
    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]
    color = board[h][w]
    height = len(board)
    width = len(board[0])
    for i in range(4):
        nh = h + dh[i]
        nw = w + dw[i]
        
        if nh >= height or nh < 0 or nw >= width or nw < 0:
            continue
            
        if board[nh][nw] == color:
            answer += 1
        
    return answer