#Check if a String Contains Only Digits
# example : "12345" is a digit, '12d' is not a digit

def contain_only_digit(input_string):
    return input_string.isdigit()

print(contain_only_digit("12345"))
print(contain_only_digit("12d"))