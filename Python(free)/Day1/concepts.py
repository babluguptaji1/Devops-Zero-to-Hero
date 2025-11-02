# This is fine?
# Yes, this is a valid Python single line comment.

"""This is also fine?
Yes, this is a valid Python multi-line comment (docstring)."""

# Variables and Constants:
my_variable = 10  # This is a variable
MY_CONSTANT = 3.14  # This is a constant by convention  

name = "Alice"  # String variable
is_active = True  # Boolean variable

# Data Types:
integer_var = 42  # Integer
float_var = 3.14  # Float
string_var = "Hello, World!"  # String
boolean_var = False  # Boolean
list_var = [1, 2, 3, 4, 5]  # List
tuple_var = (1, 2, 3)  # Tuple
dict_var = {"key1": "value1", "key2": "value2"}  # Dictionary
set_var = {1, 2, 3}  # Set
# Type Checking:
print(type(integer_var))  # <class 'int'>
print(type(string_var))   # <class 'str'>
print(type(list_var))     # <class 'list'>
print(type(dict_var))     # <class 'dict'>

# Type Conversion Or Casting:

print(float(integer_var)) # Convert integer to float output: 42.0
print(str(float_var))     # Convert float to string output: '3.14'

# Basic operators in Python:
a = 10
b = 3
# assignment operators =
c = a + b  # addition operator +
d = a - b  # subtraction operator -
e = a * b  # multiplication operator *
f = a / b  # division operator /    

print("Addition:", c)          # Output: 13
print("Subtraction:", d)       # Output: 7  
print("Multiplication:", e)    # Output: 30
print("Division:", f)          # Output: 3.3333333333333335

# comparison operators:
print("Equal:", a == b)        # Output: False
print("Not Equal:", a != b)    # Output: True
print("Greater Than:", a > b)   # Output: True
print("Less Than:", a < b)      # Output: False
print("Greater Than or Equal To:", a >= b)  # Output: True
print("Less Than or Equal To:", a <= b)     # Output: False

# Logical operators:
print("AND:", (a > 5) and (b < 5))  # Output: True
print("OR:", (a < 5) or (b < 5))    # Output: True
print("NOT:", not(a > 5))            # Output: False    


# Basic Operations:
