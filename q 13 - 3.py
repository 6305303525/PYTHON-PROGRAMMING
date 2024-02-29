def print_non_prime_numbers(A, B):
    for num in range(A + 1, B):  # Start from A+1 to exclude A and go up to B-1 to exclude B
        if num > 1:  # Prime numbers are greater than 1
            for i in range(2, int(num ** 0.5) + 1):  # Check for factors other than 1 and the number itself
                if num % i == 0:
                    print(num, end=', ')
                    break
    print()  # Just to add a newline after printing all numbers

# Sample Input
print_non_prime_numbers(12,19);
