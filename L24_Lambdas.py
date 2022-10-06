nums = [1, 2, 3, 4, 5, 6]


def square(n):
    return n * n


print(list(map(square, nums)))
# USING LAMBDA
print(list(map(lambda n: n*n, nums)))
