count =0
def dfs(v, check, graph):
    global count
    check[v] = 1
    count += 1
    for i in graph[v]:
        if check[i] == 0:
            dfs(i, check, graph)
    

def solution(n, wires):
    graph = [[] for _ in range(n+1)]
    for i in wires:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
    
    min_num = n
    
    global count
    for i in wires:
        check = [0 for _ in range(n+1)]
        check[i[1]] = 1
        count = 0
        dfs(i[0], check, graph)
        min_num = min(min_num, abs(count-(n-count)))
    return min_num
    