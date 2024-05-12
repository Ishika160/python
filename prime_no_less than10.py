def is_prime(n):

    if n <= 1:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    return True

# Print prime numbers less than 10
print("Prime numbers less than 10:")
for number in range(2, 10):
    if is_prime(number):
        print(number)
