import collections
def solution(id_list, report, k):
    answer = []
    reportHash = collections.defaultdict(set)
    stoped = collections.defaultdict(int)

    for i in range(len(report)):
        a, b = map(str, report[i].split())
        if b not in reportHash[a]:
            stoped[b] += 1
        reportHash[a].add(b)


    for name in id_list:
        mail = 0
        for user in reportHash[name]:
            if stoped[user] >= k:
                mail+=1
        answer.append(mail)
                
    return answer