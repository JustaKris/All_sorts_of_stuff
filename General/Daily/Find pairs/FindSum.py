
a_list = [10, 15, 3, 7]
k = 18

def solution(the_list, the_sum):
    for i in range(0, len(the_list)):
        for j in range(0, len(the_list)):
            if the_sum == the_list[i] + the_list[j] and i != j:
                return True
    return False

print(solution(a_list, k))