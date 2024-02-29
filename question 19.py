def binary_to_decimal(binary_str):
    decimal_val = 0
    for i in range(len(binary_str)):
        if binary_str[i] == '1':
            decimal_val += 2 ** (len(binary_str) - i - 1)
    return decimal_val
binary1 = input("Enter binary value 1: ")
binary2 = input("Enter binary value 2: ")
binary3 = input("Enter binary value 3: ")
decimal1 = binary_to_decimal(binary1)
decimal2 = binary_to_decimal(binary2)
decimal3 = binary_to_decimal(binary3)
max_decimal = max(decimal1, decimal2, decimal3)
max_binary = bin(max_decimal).replace("0b", "")
print("Maximum binary value:", max_binary)
