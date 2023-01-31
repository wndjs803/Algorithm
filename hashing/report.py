id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","muzi apeach","muzi apeach","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k =2
# id_list = ["con", "ryan"]
# report = ["ryan con", "ryan con", "ryan con", "ryan con"]
# k = 3

# 결과값 초기화
answer = [0]*len(id_list)
print(answer)
# 누가 누구를 신고했는지 확인하는 배열
name = [[id_list[i], []] for i in range(len(id_list))]
# 각 아이디마다 index 부여
index = [[id_list[i], i] for i in range(len(id_list))]
# 딕셔너리형으로 변환
name = dict(name)
# 누가 얼마나 신고를 당했는지 확인하기 위한 딕셔너리
report_result = dict()
index = dict(index)
print(index)
# report 안 요소를 list 형태로 변환
for i in range(len(report)):
    report[i] = list(report[i].split())

for i in report: # i[0] - 신고한 사람  i[1] - 신고 당한 사람
    if i[1] not in name[i[0]]: # 신고 당한 사람의 아이디가 신고한 사람의 신고리스트에 없을 시
        name[i[0]].append(i[1])
        if i[1] not in report_result: # 신고당한 사람이 얼마나 신고당했는지 확인 할 수 없다면
            report_result[i[1]] = 1 # 새로운 키값으로 배정
        else:
            report_result[i[1]] += 1 # 기존 값을 + 1

print(report_result)
# k 보다 많은 수의 신고를 받은 사람 확인하기 위한 배열
check = []
for key in report_result:
    if report_result[key] >= 2:
        check.append(key)
print(name)
# check의 요소를 얼마나 가지고 있는지 카운트 하는 반복문
for key in name:
    for i in check:
        if i in name[key]:
            answer[index[key]] += 1
print(answer)
