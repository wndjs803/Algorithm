# 이것이 코딩테스트다 with Python p.298

n, m = map(int, input().split())

parent = [0] * (n + 1)

for i in range(n):
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

for _ in range(m):
    op, a, b = map(int, input().split())

    if op == 0:
        union_parent(parent, a, b)
    if op == 1:
        if find_parent(parent, a) != find_parent(parent, b):
            print("NO")
        else: print("YES")
