import math

def lcm(a, b):
    # Calculate the least common multiple (LCM) of two numbers
    return abs(a * b) // math.gcd(a, b)

def gcd(a, b):
    # Calculate the greatest common divisor (GCD) of two numbers
    return math.gcd(a, b)

# Get input values
n = int(input("Enter the number of values: "))

# Initialize variables to store the input numbers and LCM/GCD
numbers = []
lcm_val = None
gcd_val = None

# Get input numbers and calculate LCM/GCD
for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)
    if i == 0:
        lcm_val = num
        gcd_val = num
    else:
        lcm_val = lcm(lcm_val, num)
        gcd_val = gcd(gcd_val, num)

# Print LCM and GCD
print(f"LCM: {lcm_val}")
print(f"GCD: {gcd_val}")
