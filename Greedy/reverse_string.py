s = input()
num1 = s.count("0")
num2 = s.count("1")
# s에 0과 1중 어느것이 많은가 체크
if num1 > num2: # 0이 많으면 target = 1
    target = "1"
elif num1 == 0 or num2 == 0: # 둘 중하나라도 0개면 target은 없다.
    target = ""
else:
    target ="0"

count = 0
pre=s[0]

for i in s:
    if target =="": # target이 없으므로 반복문 탈출
        break
    if (pre != i) and (i==target): # 문자가 1->0 또는 0->1로 바뀌었을 때 그 문자가 target과 같다면 교체 횟수 증가
        count += 1
    pre = i
    
print(count)