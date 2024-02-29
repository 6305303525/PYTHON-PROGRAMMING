input_string = input("Enter a string: ")
def remove_vowels(s):
    vowels = "AEIOUaeiou"
    return "".join(char for char in s if char not in vowels)
output_string = remove_vowels(input_string)
print("After removing vowels:", output_string)
