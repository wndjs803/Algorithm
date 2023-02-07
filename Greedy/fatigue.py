k = 80
dungeons = 	[[80,20],[50,40],[30,10]]

max_num = 0

answer = []

def solution(k, dungeons):
    for i in dungeons:
        global max_num
        print(answer)
        print("max_num:", max_num)
        print("k: ", k)
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

print(solution(k, dungeons))
