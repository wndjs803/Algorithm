def solution(progresses, speeds):
    answer = []
    index = 0
    
    while index != len(progresses):
        count = 0
        progresses = [a + b for a, b in zip(progresses, speeds)]
        for progresse in progresses[index:]:
            if progresse >= 100:
                count += 1
                index += 1
            else: break
        if count != 0:
            answer.append(count)
    return answer