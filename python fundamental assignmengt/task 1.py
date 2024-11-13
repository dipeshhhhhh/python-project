# Create variables of each primitive data type
int_var = 10              # Integer
float_var = 3.14          # Float
str_var = "Hello, World!" # String
bool_var = True           # Boolean

# Perform some arithmetic operations on int and float
int_addition = int_var + 20
float_addition = float_var + 1.86
int_multiplication = int_var * 2
float_multiplication = float_var * 2

# Perform string concatenation
concatenated_string = str_var + " How are you?"

# Perform logical operations on bool
bool_and = bool_var and False
bool_or = bool_var or False
bool_not = not bool_var

# Create a dictionary to store these variables categorized by their types
data_types = {
    'int': [int_var, int_addition, int_multiplication],
    'float': [float_var, float_addition, float_multiplication],
    'str': [str_var, concatenated_string],
    'bool': [bool_var, bool_and, bool_or, bool_not]
}

# Display the dictionary with values grouped by data types
print("Data Types Dictionary:")
for data_type, values in data_types.items():
    print(f"{data_type}: {values}")

# Extra: Show results of operations
print("\nResults of Operations:")
print(f"int_var + 20 = {int_addition}")
print(f"float_var + 1.86 = {float_addition}")
print(f"int_var * 2 = {int_multiplication}")
print(f"float_var * 2 = {float_multiplication}")
print(f"String concatenation: {concatenated_string}")
print(f"Logical AND (True AND False): {bool_and}")
print(f"Logical OR (True OR False): {bool_or}")
print(f"Logical NOT (NOT True): {bool_not}")
