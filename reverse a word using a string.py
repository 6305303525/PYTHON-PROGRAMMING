def reverse_word(word):
    reversed_word = ""
    for char in word:
        reversed_word = char + reversed_word
    return reversed_word

def reverse_string(input_str):
    words = input_str.split()
    reversed_words = [reverse_word(word) for word in words]
    reversed_string = " ".join(reversed_words)
    return reversed_string

# Example usage:
input_string = "TEMPLE code in python"
reversed_result = reverse_string(input_string)
print(f"Original string: {input_string}\nReversed string: {reversed_result}")
