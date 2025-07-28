
# Day 2: 30 Days of python programming

# Exercises: Level 1 -  Variables in Python
first_name = 'Le'
last_name = 'Dao'
full_name = first_name + ' ' + last_name
country = 'Vietnam'
city = 'Da Nang'
age = 34
years = 2025
is_married = True
is_light_on = False
height, weight = 1.73, 77  # in meters and kg
skills = [ 'C++', 'Java', 'Kotlin', 'Dart', 'Go', 'Android', 'iOS', 'Flutter', 'Python', 'HTML', 'CSS', 'JavaScript', 'SQL', ]
person_info = {
    'firstname':'Le', 
    'lastname':'Dao', 
    'country':'Vietnam',
    'city':'Da Nang'
    }

# Exercises: Level 2 - Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

print('Compare first name and last name length:', len(first_name) == len(last_name))
num_one,num_two = 5, 4
total = num_one + num_two
print('Sum of num_one and num_two:', total)
diff = num_one - num_two
print('Difference between num_one and num_two:', diff)
product = num_one * num_two
print('Product of num_one and num_two:', product)
division = num_one / num_two
print('Division of num_one by num_two:', division)
remainder = num_one % num_two
print('Remainder of num_one divided by num_two:', remainder)
exponent = num_one ** num_two
print('Exponent of num_one raised to num_two:', exponent)
floor_division = num_one // num_two

# Declaring multiple variables in one line
print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)