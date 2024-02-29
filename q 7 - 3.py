def remove_common_words(s1, s2):
    # Split the sentences into words
    words_s1 = set(s1.split())
    words_s2 = set(s2.split())

    # Find common words
    common_words = words_s1.intersection(words_s2)

    # Remove common words from both sentences
    result_s1 = ' '.join([word for word in s1.split() if word not in common_words])
    result_s2 = ' '.join([word for word in s2.split() if word not in common_words])

    return result_s1, result_s2

# Test cases
test_cases = [
    ("sky is blue in color", "Raj likes sky blue color"),
    ("learn python", "python is easy to learn"),
    ("raju likes apple", "apple is red in color"),
    ("sita likes orange", "orange is rich in anti-oxidents"),
    ("raj is travelling to Chennai in train", "the rain will reach Chennai at 8 pm")
]

for s1, s2 in test_cases:
    result_s1, result_s2 = remove_common_words(s1, s2)
    print(f"Input: S1 = \"{s1}\", S2 = \"{s2}\"")
    print(f"Output: {result_s1}\n        {result_s2}\n")
