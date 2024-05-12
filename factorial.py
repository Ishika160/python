def factorial(n):
    
    # Base case: factorial of 0 is 1
    if n == 0:
        return 1
    # Recursive case: factorial of n is n times factorial of (n - 1)
    else:
        return n * factorial(n - 1)

# Example usage:
number = int(input("Enter a non-negative integer: "))

result = factorial(number)
print("Factorial of", number, "is", result)
