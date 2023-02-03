import collections
import math

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

# 각각 기본 시간, 기본 요금, 단위 시간, 단위 요금
default_time = fees[0]
default_fee = fees[1]
unit_time = fees[2]
unit_fee = fees[3]

# 차가 언제 출입하는 확인하는 배열
data=[]

# 시간을 분으로 변환하는 함수
def hour_to_minute(hour, minute):
    return hour*60 + minute

for i in records:
    time, num, isIn = map(str,i.split())
    hour, minute = map(int,time.split(':'))
    # 시각을 분으로 나타낸다.
    total_minute = hour_to_minute(hour, minute)
    # 만약 주차장에 들어왔다면
    if(isIn == "IN"):
        # 차 번호와 들어온 시간을 기록
        data.append([num, total_minute])
    else: # 주차장을 나가는 것이라면
        for j in data: # 기존 data 배열
            # 나간 기록이 없고 번호가 같을 시
            if (len(j) != 3 and j[0] == num):
                # 나간 시간 기록
                j.append(total_minute)

# 누적 시간 기록하기 위한 변수           
change = collections.defaultdict(int)

for i in data:
    # 출차기록이 없을 경우 23:59으로 간주
    if (len(i) == 2):
        t = 1439 - i[1]
    else:
        t = i[2] - i[1]
    
    if i[0] not in change:
        change[i[0]] = t
    else:
        change[i[0]] += t
# 오름차순으로 정렬
change = dict(sorted(change.items()))

# 주차요금 계산
for i in change.values():
    # 누적시간이 기본 시간보다 적을 경우
    if(i <= default_time):
        print(int(default_fee))
    else:
        print(int(default_fee + (math.ceil((i-default_time)/unit_time))*unit_fee))