def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
# pls call the function and print output
print(factorial(3))
print(factorial(5))
print(factorial(7))
