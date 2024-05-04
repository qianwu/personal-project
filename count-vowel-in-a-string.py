# Count Vowels in a String:
# Write a function that takes a string as input and returns the number of vowels in that string.

def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    return count

print(count_vowels("hello"))
print(count_vowels("HeLLO"))