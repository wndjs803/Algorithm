# 이것이 코딩테스다 with Python p.395

g = int(input())
p = int(input())

gate = [False] * (g + 1)
count = 0
array = []
for _ in range(p):
    array.append(int(input()))

for index in range(p):
    value = array[index]
    check = False
    if not gate[value]:
        gate[value] = True
        check = True
    else:
        for i in range(value -1, 0, -1):
            if not gate[i]:
                gate[i] = True
                check = True
    
    if check:
        count += 1
    else: break

print(count)
