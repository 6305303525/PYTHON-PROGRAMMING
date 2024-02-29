def count_words_starting_with_A(s):
    s_lower = s.lower()
    words = s_lower.split()
    count = 0
    for word in words:
        if word.startswith("a"):
            count += 1
    return count
s = "Arun and Bob are friends. They attend an A class every day."
print(f"words starting with 'A': {count_words_starting_with_A(s)}")
