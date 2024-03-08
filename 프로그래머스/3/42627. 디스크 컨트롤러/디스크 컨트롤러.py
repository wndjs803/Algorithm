from collections import deque

def solution(jobs):
    length = len(jobs)
    jobs.sort()
    jobs = deque(jobs)
    schedule = []
    time = 0
    total = 0
    
    while jobs or schedule:
        while jobs and jobs[0][0] <= time:
            schedule.append(jobs.popleft())

        if len(schedule) > 1:
            schedule.sort(key = lambda x:x[1])

        if schedule:
            job = schedule.pop(0)

            if time < job[0]:
                time = job[0]
            time += job[1]
            total += time - job[0]
        else: time += 1
    
    return int(total/length)