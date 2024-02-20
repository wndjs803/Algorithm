def solution(bandage, health, attacks):
    answer = 0
    cur_health = health
    attack_time = attacks[0][0]
    cur_health -= attacks[0][1]
    attacks.pop(0)
    heal_time = 0
    
    while True:
        if cur_health <= 0:
            return -1
        if len(attacks) == 0:
            break
        attack_time += 1
        if attacks[0][0] == attack_time:
            cur_health -= attacks[0][1]
            heal_time = 0
            attacks.pop(0)
            continue
        
        
        
        if cur_health < health and cur_health > 0:
            heal_time += 1
            cur_health += bandage[1]
            if heal_time == bandage[0]:
                cur_health += bandage[2]
                heal_time = 0
            if cur_health > health:
                cur_health = health
                
    return cur_health