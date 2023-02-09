max_num = 0

answer = []
def solution(k, dungeons):
    for i in dungeons:
        global max_num
        if i not in answer:
            if k >= i[0]:
                k -= i[1]
                answer.append(i)
                if len(answer) >= max_num:
                    max_num =len(answer)
                solution(k, dungeons)
                answer.pop()
                k += i[1]
    return max_num