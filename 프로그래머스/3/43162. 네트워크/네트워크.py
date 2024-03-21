def solution(n, computers):
    visited = [False for _ in range(n)]
    check = []
    def dfs(cur, index):
        if visited[cur] == True:
            return
        check[index] += 1
        visited[cur] = True
        
        for i, j in enumerate(computers[cur]):
            if cur != i and computers[cur][i] != 0 and not visited[i]:
                
                dfs(i, index)
    
    for i in range(n):
        check.append(0)
        dfs(i, i)
    
    network = sum(1 for elem in check if elem != 0)
    return network