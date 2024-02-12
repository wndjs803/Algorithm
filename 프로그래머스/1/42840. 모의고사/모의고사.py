def solution(answers):
    i = 0
    count = 0
    result = []
    
    answer_1 = [1, 2, 3, 4, 5]
    for answer in answers:
        if answer == answer_1[i]:
            count += 1
        i = (i+1)%len(answer_1)
    
    result.append((1, count))
    
    count = 0
    answer_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    i = 0
    
    for answer in answers:        
        if answer == answer_2[i]:
            count += 1
        i = (i+1)%len(answer_2)
    result.append((2, count))
            
    count = 0
    answer_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    i = 0
    for answer in answers:
        if answer == answer_3[i]:
            count += 1
        i = (i+1)%len(answer_3)

    result.append((3, count))
    
    max_count = max(item[1] for item in result)
    result = [item[0] for item in result if item[1] == max_count]
    result = sorted(result)
    
    return result