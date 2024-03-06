from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    bridge = deque([0] * (bridge_length), maxlen=bridge_length)
    
    time = 1
    
    total = 0
    while truck_weights:
        time += 1
        truck = truck_weights[0]
        if total + truck <= weight:
            bridge.append(truck_weights.popleft())
            total += truck
        else: 
            bridge.append(0)
        
        total -= bridge.popleft()
    
    return time + len(bridge)