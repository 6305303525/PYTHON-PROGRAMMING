def minDistance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize first column and first row
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Fill dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]  # No operation needed
            else:
                dp[i][j] = 1 + min(dp[i-1][j],    # Delete
                                   dp[i][j-1],    # Insert
                                   dp[i-1][j-1])  # Replace
    return dp[m][n]

# Test cases
test_cases = [
    ("horse", "ros"),
    ("intention", "execution"),
    ("sunday", "saturday"),
    ("cat", "cut"),
    ("girl", "grill"),
]

# Applying function to each test case
results = [minDistance(tc[0], tc[1]) for tc in test_cases]

# Displaying results for each test case
for i, result in enumerate(results, start=1):
    print(f"Test Case {i}: Input: word1 = '{test_cases[i-1][0]}', word2 = '{test_cases[i-1][1]}'")
    print(f"Output: {result}\n")
