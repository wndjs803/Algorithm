s = input()
num0 = 0 # 1 -> 0 카운트
num1 = 0 # 0 -> 1 카운트

# pre는 처음 숫자로 지정 후 카운트 증가
pre = s[0]
if pre == "0":
    num0 += 1
else:
    num1 += 1

# 문자열 순회    
for i in s:
    # 다른 숫자로 바뀌는 걸 카운트
    if(pre != i):
        if i=="0":
            num0 += 1
        else:
            num1 += 1
    pre = i

# 둘 중 적게 카운트 된 것을 출력
print(min(num0, num1))