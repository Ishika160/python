def fibonacci_recursive(n):
    """
    Generate the n-th Fibonacci number using recursive approach.
    """
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
n = int(input("Enter the value of n to generate the n-th Fibonacci number: "))

fib_recursive = fibonacci_recursive(n)
print(f"The {n}-th Fibonacci number (recursive):", fib_recursive)