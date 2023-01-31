import collections
id_list = ["muzi", "frodo", "apeach", "neo"]
report =["muzi frodo","muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k =2
# id_list = ["con", "ryan"]
# report = ["ryan con", "ryan con", "ryan con", "ryan con"]
# k = 3
answer = []
reportHash = collections.defaultdict(set)
stoped = collections.defaultdict(int)

for i in range(len(report)):
    a, b = map(str, report[i].split())
    if b not in reportHash[a]:
        stoped[b] += 1
    reportHash[a].add(b)
print(reportHash)
print(stoped)

for name in id_list:
    mail = 0
    for user in reportHash[name]:
        if stoped[user] >= k:
            mail+=1
    answer.append(mail)

print(answer)