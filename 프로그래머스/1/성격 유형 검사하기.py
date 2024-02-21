from collections import defaultdict

def solution(survey, choices):
    answer = ''
    indicators = [('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N')]
    point = defaultdict(int)
    
    for i in range(len(survey)):
        first = survey[i][0]
        second = survey[i][1]
        
        if choices[i] < 4:
            point[first] += (4 - choices[i])
        elif choices[i] > 4:
            point[second] += (choices[i] - 4)
            
    for personality in indicators:
        first_personality = personality[0]
        second_personality = personality[1]
        
        if point[first_personality] >= point[second_personality]:
            answer += first_personality
        else:
            answer += second_personality
    return answer
