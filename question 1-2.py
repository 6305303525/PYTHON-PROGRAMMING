def isValid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if stack == [] or mapping[char] != stack.pop():
                return False
        else:
            return False

    return stack == []

# Get the input string from the user
input_string = input("Enter a string containing only the characters '(', ')', '{', '}', '[' and ']': ")

# Check if the input string is valid
result = isValid(input_string)

# Print the result
if result:
    print("true.")
else:
    print("false.")
