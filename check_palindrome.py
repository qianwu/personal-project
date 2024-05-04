### Check if a string is a palindrome
"""
"radar" is a palindrome
"madam" is a palindrome
"level" is a palindrome
"12321" is a palindrome
"""
def is_palindrome(str):
    return str == str[::-1]

def find_palindrome_in_range(range_start, range_end):
    number=[]
    for i in range(range_start, range_end):
        if is_palindrome(str(i)):
            number.append(i)
    return number

print(is_palindrome("radar"))
print(is_palindrome("madam"))

print(find_palindrome_in_range(10,1000))

# check if two lists are identical
def is_identical(list1,list2):
    return list1 == list2
list1 = [1,2,3]
list2 = [1,2,3]
print(is_identical(list1,list2))