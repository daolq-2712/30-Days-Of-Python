# Declaring the variable at the top first

age = 34 # age is a variable name and 34 is an integer data type
height = 1.73 # height is a variable name and 1.73 is a float data type

# Enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base = float(input('Enter the base of the triangle: '))  # Prompting user for base
height = float(input('Enter the height of the triangle: '))  # Prompting user for height
area_of_triangle = 0.5 * base * height  # Calculating area
print('The area of the triangle is', int(area_of_triangle))  # Printing the area

# Enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
side_a = float(input('Enter side a of the triangle: '))  # Prompting user for side a
side_b = float(input('Enter side b of the triangle: '))  # Prompting user for side b
side_c = float(input('Enter side c of the triangle: '))  # Prompting user for side c
perimeter_of_triangle = side_a + side_b + side_c  # Calculating perimeter
print('The perimeter of the triangle is', int(perimeter_of_triangle))  # Printing the perimeter

# Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radius = float(input('Enter the radius of the circle: '))  # Prompting user for radius
pi = 3.14  # Defining pi
area_of_circle = pi * radius * radius  # Calculating area
circumference_of_circle = 2 * pi * radius  # Calculating circumference
print('The area of the circle is', int(area_of_circle))  # Printing the area
print('The circumference of the circle is', int(circumference_of_circle))  # Printing the circumference

# Check if int('9.8') is equal to 10
try:
    result = int('9.8')  # Attempting to convert '9.8' to an integer
except ValueError:
    result = 'Error: Cannot convert string to integer'
print(result)  # Printing the result of the conversion attempt