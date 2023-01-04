s = input()
num0 = 0
num1 = 0

pre = s[0]
if pre == "0":
    num0 += 1
else:
    num1 += 1
    
for i in s:
    if(pre != i):
        if i=="0":
            num0 += 1
        else:
            num1 += 1
    pre = i
# print("num0: " + str(num0))
# print("num1: " + str(num1))
print(min(num0, num1))