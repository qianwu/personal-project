"""Reverse a String: Write a function that takes a string as input 
and returns the string reversed.
"""
#sample_string = "hello"
#expected_output = "olleh"
def reverse_string(input_string):
    reversed_string = ""
    for char in input_string[::-1]:
        reversed_string += char
    return reversed_string

print(reverse_string("hello")) 
print(reverse_string("hello world"))
print(reverse_string("hello world !"))     