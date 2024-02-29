import random

def check_string_palindrome():
    input_string = input("Enter a string: ")
    if input_string == input_string[::-1]:
        print("The given string is a palindrome.")
    else:
        print("The given string is not a palindrome.")

def check_number_palindrome():
    input_number = input("Enter a number: ")
    if input_number == input_number[::-1]:
        print("The given number is a palindrome.")
    else:
        print("The given number is not a palindrome.")
choice = random.choice([1, 2])
if choice == 1:
    check_string_palindrome()
else:
    check_number_palindrome()
