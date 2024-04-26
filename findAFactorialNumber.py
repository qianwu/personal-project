"""Find the Factorial of a Number: Write a function that takes a number 
as input and returns the factorial of that number."""
import math
#sample_number = 5
#expected_output = 120

def find_factorial(input_number):
    return math.factorial(input_number)


def find_factorial2(input_number):
    if input_number == 0:
        return 1
    else:
        return input_number * find_factorial2(input_number - 1)

print(find_factorial(0))
print(find_factorial2(0))