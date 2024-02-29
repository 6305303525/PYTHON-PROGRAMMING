def is_prime(n):
    """Returns True if the given number is prime, False otherwise."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
num = int(input("Enter a number: "))
result = is_prime(num)
if result:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
