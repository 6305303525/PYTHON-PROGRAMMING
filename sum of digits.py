def digit_sum(n):
    # Function to calculate the sum of digits
    return sum(map(int, str(n)))

def single_digit_sum(num):
    # Function to ensure the result is a single-digit sum
    while num >= 10:
        num = digit_sum(num)
    return num

# Example usage:
N = int(input("Enter N value: "))
number = int(input(f"Enter {N} digit number: "))

sum_of_digits = digit_sum(number)
result = single_digit_sum(sum_of_digits)

print(f"Sum of digits: {sum_of_digits}\nSingle-digit sum: {result}")
