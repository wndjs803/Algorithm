import collections
id_list = ["muzi", "frodo", "apeach", "neo"]
report =["muzi frodo","muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k =2
# id_list = ["con", "ryan"]
# report = ["ryan con", "ryan con", "ryan con", "ryan con"]
# k = 3
answer = []
# 누가 누구를 신고했는지 확인할 수 있는 변수
reportHash = collections.defaultdict(set)
# 누가 얼마나 신고를 당했나 알 수 있는 변수
stoped = collections.defaultdict(int)

for i in range(len(report)):
    # a - 신고한 사람  b - 신고 당한 사람
    a, b = map(str, report[i].split())
    # 한 사람이 똑같은 사람을 여러번 신고해도 한 번만 카운트 된다.
    if b not in reportHash[a]:
        stoped[b] += 1
    reportHash[a].add(b)


for name in id_list:
    mail = 0
    for user in reportHash[name]:
        # 일정 횟수 이상 신고당한 사람이 있을 시
        if stoped[user] >= k:
            mail+=1
    answer.append(mail)

print(answer)