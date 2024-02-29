def is_perfect_square(num):
    square_root = int(num**0.5)
    return square_root**2 == num

def sum_of_digits_less_than_10(num):
    digit_sum = sum(int(digit) for digit in str(num))
    return digit_sum < 10

def find_perfect_squares_with_sum_less_than_10(start, end):
    result = [num for num in range(start, end + 1) if is_perfect_square(num) and sum_of_digits_less_than_10(num)]
    return result

n = int(input("entre the value of n:"))
m = int(input("entre the value of m:"))
perfect_squares = find_perfect_squares_with_sum_less_than_10(n, m)
print("Perfect squares with sum of digits less than 10:", perfect_squares)
