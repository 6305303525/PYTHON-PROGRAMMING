def count_chars_until_asterisk():
    uppercase_count = 0
    lowercase_count = 0
    number_count = 0

    while True:
        char = input("Enter a character: ")

        if char == '*':
            break

        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
        elif char.isdigit():
            number_count += 1

    return uppercase_count, lowercase_count, number_count

# Read characters and count uppercase, lowercase, and numbers
uppercase_count, lowercase_count, number_count = count_chars_until_asterisk()

# Print the results
print("Number of uppercase letters:", uppercase_count)
print("Number of lowercase letters:", lowercase_count)
print("Number of numbers:", number_count)
