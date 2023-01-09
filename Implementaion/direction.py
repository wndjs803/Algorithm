n = int(input())
data = str, input().split()

i=1
j=1

for k in data:
    if k == "R":
        if i+1 <= n:
            i +=1
    elif k == "L":
        if i-1 >= 1:
            i -= 1
    elif k == "U":
        if j-1 >= 1:
            j -= 1
    else:
        if j+1 <= n:
            j += 1

print(j, i)