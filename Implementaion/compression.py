s = "xababcdcdababcdcd"

num = 0 # 몇개 문자로 슬라이스 할 것인가
result = [] # 압축결과
a = [] # 압축결과 후보들
while num != len(s):
    num += 1
    j=0
    count = 1  # 비교 시 서로 같은 횟수
    while True:
        # num 만큼 비교하기 위해 슬라이싱을 이용해 설정한다.
        tmp = s[j:j+(num)] 
        cmp = s[j+num:j+2*num]
        # 두 문자열이 서로 같으면
        if tmp == cmp:
            count += 1
        else: # 서로 다를 시
            if count == 1: # count=1일때는 숫자를 표시하지 않는다.
                result.append(tmp)
            else:
                result.append(str(count) + tmp)
                count = 1
            # 같지 않기 때문에 tmp = cmp가 된다. 만약 두 문자가 서로 같다면 해줄 필요가 없다.
            tmp = cmp
        # 다음 문자를 비교하기 위해 인덱스를 증가시켜준다.
        j += num
        # 만약 증가한 인덱스가 기존 문자열의 길이 보다 크다면
        if j > len(s) or j+num > len(s): # 나머지 문자열을 result에 추가한다..
            if count == 1:
                result.append(s[j:len(s)])
            else:
                result.append(str(count)+s[j:len(s)])
            
            break
    b = "".join(result) # 압축결과가 list형태로 되어있기에 str로 바꿔준다.
    a.append([b, len(b)]) # 압축결과 후보에 추가한다.
    result = [] # 다음 반복문을 위해 빈 리스트로 초기화한다.

# 후보들 중 길이가 가장 작은 후보를 골라 출력한다.
print(min(a, key=lambda x :x[1])[0])