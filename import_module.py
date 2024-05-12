# my_module.py

def factorial(n):
    """
    Calculate the factorial of a non-negative integer n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# main.py

from my_module import factorial

# Example usage:
number = int(input("Enter a non-negative integer: "))

result = factorial(number)
print(f"The factorial of {number} is {result}")
