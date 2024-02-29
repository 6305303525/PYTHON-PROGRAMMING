def square_and_cube(number):
    square = number ** 2
    cube = number ** 3
    return square, cube

# Example usage:
number = int(input("Enter a number: "))
square, cube = square_and_cube(number)
print("Square of", number, "is:", square)
print("Cube of", number, "is:", cube)
