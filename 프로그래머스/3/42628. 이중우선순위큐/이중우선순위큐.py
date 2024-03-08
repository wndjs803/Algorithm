def solution(operations):
    queue = []
    for op in operations:
        command, value = op.split(" ")
        
        if command == "I":
            queue.append(int(value))
            queue.sort()
        elif command == "D" and queue:
            if value == "1":
                queue.pop(len(queue)-1)
            elif value == "-1":
                queue.pop(0)
    
    if not queue:
        return [0, 0]
    else:
        return [queue[-1], queue[0]]