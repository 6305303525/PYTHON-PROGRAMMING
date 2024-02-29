def print_numbers_except_digit(P, Q, R):
    for i in range(P, Q + 1):
        if str(R) not in str(i):
            print(i)

# Sample Input
P = 60
Q = 70
R = 3

print_numbers_except_digit(P, Q, R)

