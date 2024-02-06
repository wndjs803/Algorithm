def solution(phone_book):
    hash_map = {}
    
    for number in phone_book:
        hash_map[number] = 1
    
    for number in phone_book:
        str = ""
        for s in number:
            str += s
            if str in hash_map and str != number:
                return False
    
    return True
        
