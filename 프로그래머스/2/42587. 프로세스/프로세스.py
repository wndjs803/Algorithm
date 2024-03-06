from collections import deque

def solution(priorities, location):
    queue = deque([(i, p) for i, p in enumerate(priorities)])
    step = 0
    while True:
        cur = queue.popleft()
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            step += 1
            if cur[0] == location:
                return step
        