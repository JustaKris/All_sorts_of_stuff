
N = 4
X = {1, 3, 5}

# Solution
def staircase_1(n):
    a, b = 1, 2
    for _ in range(n - 1):
        a, b = b, a + b
    return a

print(staircase_1(N))

# Solution + X
def staircase_2(n, X):
    cache = [0 for _ in range(n + 1)]
    cache[0] = 1
    for i in range(1, n + 1):
        cache[i] += sum(cache[i - x] for x in X if i - x >= 0)
    return cache[n]

print(staircase_2(N, X))





