"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
# No setup
# repeat forever:
#     read input
#     tokenize input
#     if the first token is "q":
#         quit
#     else:
#         decide which math function to call based on first token
while True:

    user_input = input()

    tolkens = user_input.split(" ")

    num1 = int(tolkens[1])
    num2 = int(tolkens[2])

    if tolkens[0] == "q":
        exit()

    if tolkens[0] == "+":
        output = add(num1, num2)

    if tolkens[0] == "-":
        output = subtract(num1, num2)

    if tolkens[0] == "*":
        output = multiply(num1, num2)

    if tolkens[0] == "/":
        output = divide(num1, num2)

    if tolkens[0] == "square":
        output = square(num1)

    if tolkens[0] == "cube":
        output = cube(num1)

    if tolkens[0] == "power":
        output = divide(num1, num2)

    if tolkens[0] == "mod":
        output = mod(num1, num2)

    print(output)



  
