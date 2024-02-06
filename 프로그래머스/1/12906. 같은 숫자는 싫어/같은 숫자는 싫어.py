def solution(arr):
    answer = []
    check = -1
    for i in range(len(arr)):
        if check != arr[i]:
            answer.append(arr[i])
        check = arr[i]
        
        
    return answer