from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0

    truck_weights = truck_weights[::-1]
    bridge = [0] * bridge_length

    while bridge:
        answer += 1
        bridge.pop(0)
        
        if truck_weights:
            if truck_weights[-1] + sum(bridge) <= weight:
                bridge.append(truck_weights.pop())
            else:
                bridge.append(0)
        print(bridge)

    return answer

bridge_length = 3
weight = 10
truck_weights = [1,4,5,6]
print(solution(bridge_length, weight, truck_weights))