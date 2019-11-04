
array = [3, 4, -1, 1, 1, -3, 1, 3, 7, 5, 6]

def solution(an_array):
    dummy = []
    for x in an_array:
        if x > 0 and x + 1 not in an_array:
            dummy.append(x + 1)
    return min(dummy)

print(solution(array))