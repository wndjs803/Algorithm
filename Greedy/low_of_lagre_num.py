p = input().split()

n = int(p[0])
m = int(p[1])
k = int(p[2])

li = input().split()

intList = [int(x) for x in li] # ListComprehension

intList.sort(reverse=True) # list 본체를 정렬

count = 0
total = 0

for i in range(m):
    if(count <k):
        total += intList[0]
        count +=1
    else:
        total += intList[1]
        count = 0

print(total)