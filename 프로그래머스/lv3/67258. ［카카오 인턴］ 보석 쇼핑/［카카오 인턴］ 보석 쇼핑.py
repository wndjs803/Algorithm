import collections

def solution(gems):
    check = collections.defaultdict(int)
    lt = 0
    l = len(set(gems))
    max_len = 100000
    for rt in range(len(gems)):
        check[gems[rt]] +=1
        while(len(check) == l):
            if rt-lt+1 <max_len:
                max_len = rt-lt+1
                answer = [lt+1, rt+1]
                
            check[gems[lt]] -= 1
            if check[gems[lt]] == 0:
                del check[gems[lt]]
            lt += 1

    return answer
            