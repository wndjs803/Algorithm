def solution(friends, gifts):
    answer = 0
    
    data = [[0 for _ in range(len(friends))] for _ in range(len(friends))]
    friend_index = {name: index for index, name in enumerate(friends)}
    
    for gift in gifts:
        giver, receiver = gift.split(" ")
        for friend in friends:
            if giver == friend:
                data[friend_index[giver]][friend_index[receiver]] += 1
                break
    
    gift_to_receive = [0 for _ in range(len(friends))]
    
    for index_A, item_A in enumerate(friends):
        for index_B, item_B in enumerate(friends[index_A:], start=index_A):
            A_to_B = data[index_A][index_B]
            B_to_A = data[index_B][index_A]
            
            if A_to_B > B_to_A:
                gift_to_receive[index_A] += 1
            elif A_to_B < B_to_A:
                gift_to_receive[index_B] += 1
            else:
                A_received = 0
                B_received = 0
                for i in data:
                    A_received += i[index_A]
                    B_received += i[index_B]
                
                A_given = sum(data[index_A])
                B_given = sum(data[index_B])
                
                A_point = A_given - A_received
                B_point = B_given - B_received
                
                if A_point > B_point:
                    gift_to_receive[index_A] += 1
                elif A_point < B_point:
                    gift_to_receive[index_B] += 1
        
        answer = max(gift_to_receive)
    return answer
