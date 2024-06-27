# 경로 압축 기법을 적용
def find_parent(parent, x):
    if parent[x] != x: # 부모테이블에서 부모가 자기자신이 아니라는 것은 더 작은 값으로 갱신이 되었다는 것을 의미
        parent[x] = find_parent(parent, parent[x]) # 이렇게 재귀적으로 호출되다보면 최종적으로는 가장 작은 값을 가진 부모를 찾게되고 전부 그 값으로 적용됨.
    return parent[x] # 이 구문을 통해 가장 작은 값이 재귀적으로 계속 리턴됨.
    # 중요 포인트는 x를 넘기는 것이 아니라 parent[x]를 넘겨야 한다.

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    # 자신의 부모를 찾늗다.
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    # 더 작은 값을 찾아 그 값으로 갱신
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
parent = [0] * (v + 1)

# 부모 테이블에서 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

edges = []

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
edges.sort() # cost(비용)를 기준으로 오름차순 정렬
result = 0

for edge in edges:
    cost, a, b = edge
    
    if find_parent(parent, a) != find_parent(parent, b): # 루트 노트가 서로 다를 시 -> 사이클이 발생하지 않을 시
        union_parent(parent, a, b) # union 연산
        result += cost 

print(result)
