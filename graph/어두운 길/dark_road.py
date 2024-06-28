# 이것이 코딩테스다 with Python p.397

n, m = map(int, input().split())

edges = []
total_cost = 0
for _ in range(m):
    a, b, cost = map(int, input().split())
    total_cost += cost
    edges.append((cost, a, b))
edges.sort()

parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

result = 0

for edge in edges:
    cost, a, b = edge

    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(total_cost - result)
