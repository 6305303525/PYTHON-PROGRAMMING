def arrange_letters(word):
    char_list = list(word)
    char_list.sort(reverse=True)
    arranged_word = ''.join(char_list)
    return arranged_word
input_word = input("Enter a word: ")
result = arrange_letters(input_word)
print(f"The arranged word is: {result}")
