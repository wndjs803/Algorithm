def solution(s):
    left = 0
    right = 0
    
    for i in range(len(s)):
        if i == 0 and s[i] == ")":
            return False
        
        if s[i] == "(":
            left += 1
        else: right += 1
        
        if right > left: return False
    
    if right != left: return False
    return True