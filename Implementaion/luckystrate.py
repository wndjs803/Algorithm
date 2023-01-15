n = list(map(int, input()))
l = len(n)

sum1, sum2 = 0, 0

for i in range(l):
    if (i < l/2):
        sum1 += n[i]
    else:
        sum2 += n[i]
        
# print(sum1, sum2)

if(sum1 == sum2):
    print("LUCKY")
else:
    print("READY")