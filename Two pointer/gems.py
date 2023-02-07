import collections

gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
# gems = ["AA", "AB", "AC", "AA", "AC"]
# gems = ["XYZ", "XYZ", "XYZ"]
# gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]



def solution(gems):
	# 보석 종류와 각 보석의 개수를 체크하기 위함.
    check = collections.defaultdict(int)
    lt = 0
	# set을 이용해 보석 종류의 개수를 알 수 있다.
    l = len(set(gems))
	# 최대길이 설정
    max_len = 100000

    for rt in range(len(gems)):
		# rt로 순회하며 보석의 종류와 개수를 증가시킨다.
        check[gems[rt]] +=1
		# 만약 key의 개수가 보석의 종류와 같다면 lt로 순회
        while(len(check) == l):
			# 만약 현재 구간의 길이가 최대길이 보다 작다면 수정한다.
            if rt-lt+1 <max_len:
                max_len = rt-lt+1
                answer = [lt+1, rt+1]
            # lt로 순회하면서 보석의 개수를 줄인다.
            check[gems[lt]] -= 1
			# 만약 보석의 개수가 0이라면 key를 제거한다.
            if check[gems[lt]] == 0:
                del check[gems[lt]]
            lt += 1
    return answer
