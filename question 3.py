def find_MSD_LSD(num):
    num_str = str(num)
    if len(num_str) == 1:
        return f"MSD: {num_str}, LSD: {num_str}"
    MSD = next((digit for digit in num_str if digit != '0'), '0')
    LSD = num_str[-1]
    return f"MSD: {MSD}, LSD: {LSD}"
decimal_num = input("Enter a decimal number: ")
if decimal_num.isdigit():
    decimal_num = int(decimal_num)
    print(find_MSD_LSD(decimal_num))
else:
    print("Invalid input. Please enter a valid decimal number.")
