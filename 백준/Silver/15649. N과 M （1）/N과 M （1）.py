n, m = map(int, input().split())

answer = []

def dfs():
    if (len(answer) == m):
        for i in answer:
            print(i, end=" ")
        print()
        return
    
    for i in range(1, n+1):
        if i not in answer:
            answer.append(i)
            dfs()
            answer.pop()
        
dfs()