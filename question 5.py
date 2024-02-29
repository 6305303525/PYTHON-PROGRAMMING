def count_vowels(statement):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    vowel_count = 0
    for char in statement:
        if char.lower() in vowels:
            vowel_count += 1
    return vowel_count
input_statement = input("Enter a statement: ")
result = count_vowels(input_statement)
print(f"The number of vowels in the statement is: {result}")
