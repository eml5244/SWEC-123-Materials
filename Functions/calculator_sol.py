"""
A program that calculates answers to an arthimetic problem. The students should start by creating a module called "calculator.py".
    Their module should create 4 functions, add, subtract, multiply, and divide, that each take two numbers.
        The two numbers and operator will be inputted by the user in main and passed into the function calls there as arguments.
        Each function should return the calculation of the two numbers after casting the string inputs to floats (can happen in each function or in main).
            The students do not need to worry about negatives or dividing by 0
    Print the result of each function call in main, in the formating "<num1> (+,-,*,/) <num2> = <return_value>.

Created by Emma Lubes, eml5244, for the Academic Success Center Supplemental Instruction Program.
"""

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def main():
    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter another number: "))
    added = add(num1, num2)
    subtracted = subtract(num1, num2)
    multiplied = multiply(num1, num2)
    divided = divide(num1, num2)

    print(num1, " + ", num2, " = ", added, sep="")
    print(num1, " - ", num2, " = ", subtracted, sep="")
    print(num1, " * ", num2, " = ", multiplied, sep="")
    print(num1, " / ", num2, " = ", divided, sep="")

main()