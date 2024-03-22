from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    queue = deque()
    queue.append([begin, 0])
    
    while queue:
        cur_word, step = queue.popleft()
        
        if cur_word == target:
            return step
        
        for word in words:
            count = 0
            for i in range(len(word)):
                if cur_word[i] != word[i]:
                    count += 1
                    
            if count == 1:
                queue.append([word, step+1])
    return 0