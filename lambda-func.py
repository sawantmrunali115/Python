# Printing the result by calling the lambda function with positional arguments
add = lambda a,b: a + b
print(add(5, 3))  

# Printing the result by calling the lambda function with keyword arguments
sub = lambda a,b: a - b
print(sub(b=8, a=15))

# Printing the result by calling the lambda function with a default argument
multiply = lambda a, b=2: a * b
print(multiply(4))

# Printing the result by calling the lambda function with variable number of arguments
addition = lambda *arg: sum(arg)
print(addition(1, 2, 3, 4, 5))

# Calling the lambda function with an argument
print((lambda x: (x%2 and "Even" or "Odd"))(10))

# Printing the result by calling the lambda function with a string argument
sub_string = lambda string: string in "Hello, World!"
print(sub_string("Hello")) 