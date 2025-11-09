def factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return n * factorial(n-1)

num = int(input("Enter a number: "))
result = factorial(num)
print(f"Factorial of {num} is {result}")