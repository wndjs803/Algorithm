k = 80
dungeons = 	[[80,20],[50,40],[30,10]]

max_num = 0
# 던전의 순서를 저장하는 배열
answer = []

def solution(k, dungeons):
    for i in dungeons:
        # 탐험할 수 있는 최대의 던전 수
        global max_num
        # 해당하는 던전이 아직 포함되지 않았따면
        if i not in answer:
            # 현재 피로도가 최소 필요 피로도보다 같거나 높다면
            if k >= i[0]:
                # 필요 피로도만큼 뺸다.
                k -= i[1]
                # 던전 순서에 포함 시킨다.
                answer.append(i)
                # 던전의 최대 값을 비교한다.
                if len(answer) >= max_num:
                    max_num =len(answer)
                # 다시 dfs를 활용한다.
                solution(k, dungeons)
                # 마지막 던전을 순서에서 제외시킨다.
                answer.pop()
                # 제외시킨만큼 피로도를 회복시킨다.
                k += i[1]
    return max_num

print(solution(k, dungeons))
