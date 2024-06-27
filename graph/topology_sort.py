from collections import deque

v, e = map(int, input().split())
indegree = [0] * (v + 1) # 진입 차수를 저장할 배열
graph = [[] for i in range(v + 1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b) # a->b
    indegree[b] += 1 # b로 진입할 수 있는 경우의 수 증가

def topology_sort():
    result = []
    q = deque()

    for i in range(1, v + 1):
        if indegree[i] == 0: # 진입 차수가 0인 번호를 모두 큐에 넣는다.
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now) # 큐에서 나오는 순서대로 정렬된 것

        for i in graph[now]:
            indegree[i] -= 1 # now가 빠졌으므로 진입 차수가 감소
            if indegree[i] == 0:
                q.append(i)
    
    print(result)

topology_sort()
