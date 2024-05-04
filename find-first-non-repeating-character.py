# Given a string, find the first non-repeating character and return its index. If it doesn't exist, return -1.
# Examples: apple -> 0, leetcode -> 0, loveleetcode -> 2, aabb -> -1
# Constraints: The characters in the string can be alphanumeric and may include spaces and punctuation.

def find_first_non_repeating_character(input_string):
    char_count = {}
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for i in range(len(input_string)):
        if char_count[input_string[i]] == 1:
            return i
    return -1

print(find_first_non_repeating_character("apple"))