from itertools import permutations
import math

def solution(numbers):
    nums = [num for num in numbers]
    p = []
    for i in range(1, len(nums)+1):
        p += list(permutations(nums, i))
    new_nums = [int("".join(value)) for value in p]
    result = set()
    
    for num in new_nums:
        check = True
        if num < 2:
            continue
        else:
            r = int(math.sqrt(num))
            for i in range(2, r+1):
                if num%i == 0:
                    check = False
                    break
        if check:
            result.add(num)

    return len(result)