from collections import deque

def solution(maps):
    # 하, 우, 상, 좌
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    queue = deque()
    queue.append((0,0))
    
    while queue:
        cur = queue.popleft()
        cur_row, cur_col = cur[0], cur[1]
        
        for i in range(4):
            new_row = cur_row + dx[i]
            new_col = cur_col + dy[i]
            
            if new_row >=0 and new_row < len(maps) and new_col >= 0 and new_col < len(maps[0]):
                if maps[new_row][new_col] == 1:
                    maps[new_row][new_col] += maps[cur_row][cur_col]
                    queue.append((new_row, new_col))
        
    answer = maps[-1][-1]
    if answer == 1:
        return -1
    else:
        return answer