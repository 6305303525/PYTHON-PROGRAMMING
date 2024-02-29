def calculate_circle_area(radius):
   import math
   area = math.pi * (radius ** 2)
   return area
radius = float(input("Enter the radius of the circle: "))
area = calculate_circle_area(radius)
print(f"Area = {area}")
