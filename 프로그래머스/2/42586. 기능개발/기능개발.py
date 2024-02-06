import math

def solution(progresses, speeds):
    answer = []
    days = []
    for i in range(len(speeds)):
        left_prog = 100.0 - progresses[i]
        day = math.ceil(left_prog/speeds[i])
        days.append(day)

    max_day = days[0]
    count = 1
    
    for i in range(1, len(days)):
        if max_day < days[i]:
            max_day = days[i]
            answer.append(count)
            count = 1
        else: count += 1
    
    answer.append(count)
    return answer