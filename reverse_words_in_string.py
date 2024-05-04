# reverse words in a string
def reverse_words(s):
    #return ' '.join(reversed(s.split()))
    return ''.join(s.split()[::-1])

# reverse a list

def reverse_list(s_list):
    reversed_list = reversed(s_list)
    return list(reversed_list)

print(reverse_words("hello world"))
print(reverse_list(["hello", "world"]))