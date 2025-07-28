# Introduction
# Day 1 - 30DaysOfPython Challenge

print(3 + 4)   # addition(+)
print(3 - 4)   # subtraction(-)
print(3 * 4)   # multiplication(*)
print(3 / 4)   # division(/)
print(3 ** 4)  # exponential(**)
print(3 % 4)   # modulus(%)
print(3 // 4)  # Floor division operator(//)

# Checking data types
print(type(10))                  # Int
print(type(3.14))                # Float
print(type(1 + 3j))              # Complex
print(type('Asabeneh'))          # String
print(type(True))                # Bool
print(type([1, 2, 3]))           # List
print(type({'name':'Asabeneh'})) # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple
print(type(3 == 3))              # Bool
print(type(3 >= 3))              # Bool

# Euclidian distance between (2, 3) and (10, 8)
import math
x1, y1 = 2, 3
x2, y2 = 10, 8
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(f"Euclidian distance: {distance}")
