from collections import defaultdict

def solution(participant, completion):
    participant_dict = defaultdict(int)  # int의 기본값은 0

    for i in participant:
        participant_dict[i] += 1
    
    for i in completion:
        participant_dict[i] -= 1

    answer = [key for key in participant_dict if participant_dict[key] == 1]
    
    return answer[0]
