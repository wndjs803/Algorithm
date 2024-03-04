def solution(phone_book):
    # 전부 키, 밸류로 만든다.
    phone_number = {}
    
    for num in phone_book:
        phone_number[num] = 0
    
    for key in phone_number.keys():
        jubdoo = ""
        for s in key:
            jubdoo += s
            
            if jubdoo == key:
                break
                
            if jubdoo in phone_number.keys():
                return False
    
    return True
