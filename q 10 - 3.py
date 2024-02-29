def isScramble(s1, s2):
    if len(s1) != len(s2):
        return False
    if s1 == s2:
        return True
    if sorted(s1) != sorted(s2):
        return False

    for i in range(1, len(s1)):
        # Check if there's a valid split where the first halves match or the first half of one matches the second half of the other
        if (isScramble(s1[:i], s2[:i]) and isScramble(s1[i:], s2[i:])) or \
           (isScramble(s1[:i], s2[-i:]) and isScramble(s1[i:], s2[:-i])):
            return True
    return False

# Test cases
test_cases = [
    ("great", "eatgr"),
    ("abcde", "caebd"),
    ("a", "a"),
    ("ab", "ad"),
    ("10", "-5")
]

results = [isScramble(tc[0], tc[1]) for tc in test_cases]

for i, (s1, s2) in enumerate(test_cases):
    print(f'Test case {i+1}: s1="{s1}", s2="{s2}", Result: {results[i]}')
