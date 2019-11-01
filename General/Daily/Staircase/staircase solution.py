
N = 4
X = {1, 3, 5}

# Slution
def solution(n):
    if n == 0 or n == 1:
        return 1
    nums = []
    for x in range(1, n+2):
        nums.append(x)
    # print(nums)
    nums[0] = 1
    nums[1] = 1
    for i in range(2, n):
        nums[i] = nums[i-1] + nums[i-2]
    # print(nums)
    return nums[n]

print(solution(N))

# Solution with X
def solution_X(n, X):
    if n == 0:
        return 1
    nums = []
    for x in range(1, n + 2):
        nums.append(x)
    # print(nums)
    nums[0] = 1
    for i in range(1, n+1):
        total = 0
        for j in X:
            if i - j >= 0:
                total += nums[i - j]
        nums[i] = total
    return nums[n]

print(solution_X(N, X))
