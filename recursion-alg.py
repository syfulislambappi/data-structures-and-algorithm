# Basics of recursion
def recursion(n):
    if n == 0:
        return
    recursion(n - 1)
    print(n)

# recursion(5)

# Recursion Tree
def rec_tree(n):
    if n == 0:
        return

    print(n)
    rec_tree(n - 1)
    rec_tree(n - 1)

# rec_tree(5)

# Calculate factorial
def factorial(n):
    if n <= 1:
        return 1

    return factorial(n - 1) * n

# print(factorial(5))

# Fibonacci Series
def fib_series(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_series(n - 1) + fib_series(n - 2)

print(fib_series(7))