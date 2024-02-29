def list_of_tuples(lower, upper):
    # Check if lower range is greater than upper range
    if lower > upper:
        return "Lower range must be less than or equal to upper range."

    # Generate list of tuples (number, square of number)
    return [(i, i**2) for i in range(lower, upper + 1)]

# Example usage
lower = int(input("Enter the lower range: "))
upper = int(input("Enter the upper range: "))

result = list_of_tuples(lower, upper)
print(result)
