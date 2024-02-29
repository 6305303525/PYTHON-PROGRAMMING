def count_special_characters(statement):
    count = 0
    for char in statement:
        if not char.isalnum():
            count += 1
    return count

# Example usage:
statement = "Hello, World! @#"
result = count_special_characters(statement)
print("Number of special characters:", result)
