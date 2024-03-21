from collections import deque
row, col = map(int, input().split())

graph = []

for i in range(row):
    graph.append(list(map(int, input())))

# 하, 우, 상, 좌
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

queue = deque()
queue.append((0, 0))

while queue:
    cur = queue.popleft()
    cur_row, cur_col = cur[0], cur[1]

    for i in range(4):
        new_col = cur_col + dx[i]
        new_row = cur_row + dy[i]

        if new_col >= 0 and new_col < col and new_row >= 0 and new_row < row:
            if graph[new_row][new_col] == 1:
                graph[new_row][new_col] += graph[cur_row][cur_col]
                queue.append((new_row, new_col))

print(graph[-1][-1])