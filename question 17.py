sentence = input("Enter a sentence: ")
words = sentence.split()
modified_words = []
for word in words:
    modified_word = word[0].upper() + word[1:]
    modified_words.append(modified_word)
result = '.'.join(modified_words)
print("Output:", result)
