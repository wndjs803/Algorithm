s = list(map(int, input()))# list()를 통해 문자 리스트를 만들 수 있다.
total = s[0] # 초기값을 s의 제일 처음 값으로 지정한다.
n = len(s)-1 # s의 마지막 index

for i in range(1, n): # 초기값을 s[0]으로 지정했기에 1부터 시작
    if s[i] <= 1 or s[i+1] <=1 or total <=1: # s[i], s[i+1], total 이 셋 중 어느하나라도 1이하면 더해야 숫자가 더 커질 수 있다.
        total += s[i]
    else:
        total *= s[i]
    print(total)

# index error를 막기위해 마지막 index는 따로 처리한다.
if s[n] <= 1:
    total += s[n]
else:
    total *= s[n]
    
print(total)