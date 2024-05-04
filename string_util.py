
class string_solution:
    def __init__(self,string):
        self.string = string

    def count_vowels(self,input_string):
        vowels = "aeiouAEIOU"
        count = 0
        for char in input_string:
            if char in vowels:
                count += 1
        return count
    
    # compare two strings
    def compare_strings(self,s1, s2):
        return s1 == s2
    
    #compare two strings ignoring case
    def compare_strings_ignore_case(self,s1, s2):
        return s1.lower() == s2.lower()
    # compare two strings ignoring case and orders
    def compare_strings_ignore_case_and_order(self,s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    
    # check if a string is a pangram
    def is_pangrams(self,s):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for char in alphabet:
            if char not in s.lower():
                return False
        return True
    
    # convert data to string
    def convert_to_string(self,data):
        return str(data)
    
    # find string in json string
    def find_string_in_json(self,json_string, string):
        return string in json_string

    # compare partial string in a string with random number
    # eg : compare_partial_string_with_random_number("identify12344", "identify2543433") -> True
    def compare_partial_string_with_random_number(self,string1, string2):
        for i in string1:
            if i.isdigit():
                if i in string2:
                    return True
        return False


string_util = string_solution("test")
print(string_util.count_vowels("hello"))
print(string_util.compare_strings("hello","olleh"))
print(string_util.compare_strings_ignore_case("hello","Olleh"))
print(string_util.compare_strings_ignore_case_and_order("hello","Olleh"))
    