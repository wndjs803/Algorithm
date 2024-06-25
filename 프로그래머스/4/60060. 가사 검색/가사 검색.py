from bisect import *

def count_by_range(array, left_vlaue, right_value):
    left_index = bisect_left(array, left_vlaue)
    right_index = bisect_right(array, right_value)

    return right_index - left_index

result = []
array = [[] for _ in range(10001)]
reversed_array = [[] for _ in range(10001)]

def solution(words, queries):
    for word in words:
        array[len(word)].append(word)
        reversed_array[len(word)].append(word[::-1])
    
    for i in range(10001):
        array[i].sort()
        reversed_array[i].sort()

    for query in queries:
        if query[0] != "?":
            count = count_by_range(array[len(query)], query.replace("?", "a"), query.replace("?", "z"))
        else:
            count = count_by_range(reversed_array[len(query)], query[::-1].replace("?", "a"), query[::-1].replace("?", "z"))
        result.append(count)
    return result