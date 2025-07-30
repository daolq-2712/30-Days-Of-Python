# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
first_string = 'Thirty'
second_string = 'Days'
third_string = 'Of'
fourth_string = 'Python'
space = ' '
full_string = first_string + space + second_string + space + third_string + space + fourth_string
print(full_string)

# Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"
print(company)
print(len(company))
print(company.upper() + " ==/== " + company.lower())

# List contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
#define a list of libraries
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
#join the list with a hash and space
joined_libraries = ' # '.join(libraries)
print(joined_libraries)

radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")
