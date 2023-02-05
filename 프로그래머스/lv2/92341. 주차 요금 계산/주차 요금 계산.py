import collections
import math

def solution(fees, records):
    default_time = fees[0]
    default_fee = fees[1]
    unit_time = fees[2]
    unit_fee = fees[3]

    data=[]

    def hour_to_minute(hour, minute):
        return hour*60 + minute

    for i in records:
        time, num, isIn = map(str,i.split())
        hour, minute = map(int,time.split(':'))
        total_minute = hour_to_minute(hour, minute)
        if(isIn == "IN"):
            data.append([num, total_minute])
        else:
            for j in data:
                if (len(j) != 3 and j[0] == num):
                    j.append(total_minute)

    
    change = collections.defaultdict(int)

    for i in data:
        if (len(i) == 2):
            t = 1439 - i[1]
        else:
            t = i[2] - i[1]

        if i[0] not in change:
            change[i[0]] = t
        else:
            change[i[0]] += t
    change = dict(sorted(change.items()))

    answer = []

    for i in change.values():
        if(i <= default_time):
            answer.append(int(default_fee))
        else:
            answer.append(int(default_fee + (math.ceil((i-default_time)/unit_time))*unit_fee))
    
    return answer