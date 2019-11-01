
array = [1, 2, 3, 4, 5]

def solution(base_array):
    product_array = []
    for i in range(0, len(base_array)):
        work_array = []
        for j in base_array:
            if j != base_array[i]:
                work_array.append(j)
        # print(work_array)
        product = 1
        for x in work_array:
            product = product * x
        product_array.append(product)
        # print(product)

    return product_array


print(solution(array))

'''
array2 = [3, 2, 1]
print(solution(array2))

array3 = [15, 215, 4, 11, 3]
print(solution(array3))
'''
