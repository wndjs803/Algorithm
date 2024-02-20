def solution(data, ext, val_ext, sort_by):
    answer = []
    
    index = {'code': 0, 'date': 1, 'maximum': 2, 'remain': 3}
    
    for info in data:
        if info[index[ext]] < val_ext:
            answer.append(info)
    
    answer.sort(key=lambda x: x[index[sort_by]])
    return answer