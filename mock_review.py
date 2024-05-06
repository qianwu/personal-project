# Write a Python function to check if a string is a palindrome.
def check_string_is_palindrome(input_string):
    return input_string == input_string[::-1]


# inplement a funtion to find the first non-repeating character in a string
def find_first_non_repeating_character(str):
    # create a dictionary to store the count of each character
    char_count = {}
    # iterate through the string and count the occurrence of each character
    for char in str:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    # find the first character with count 1
    for char in str:
        if char_count[char] == 1:
            return char
        return None


def find_first_non_repeating_character_by_set(str):
    repeated_chars = set()
    non_repeated_chars = set()
    for char in str:
        if char in non_repeated_chars:
            non_repeated_chars.remove(char)
            repeated_chars.add(char)
        elif char not in repeated_chars:
            non_repeated_chars.add(char)
    for char in str:
        if char in non_repeated_chars:
            return char
    return None


# Given a list of integers, write a function in Python to \n
# find the maximum difference between any two numbers in the list.
# For example, if the input is [1, 2, 3, 8, 9], the output should be 7.
def find_max_difference(numbers):
    if len(numbers) < 2:
        return None
    min_num = numbers[0]
    max_diff = 0
    for num in numbers:
        if num < min_num:
            min_num = num
        if num - min_num > max_diff:
            max_diff = num - min_num
    return max_diff


def test_find_max_difference():
    assert find_max_difference([1]) is None
    assert find_max_difference([1, 0, 4, 9, 10]) == 10
    assert find_max_difference([1, 0, 4, 9, 10, 11, 11]) == 11


# Implement a function in Python to sort an array of integers in ascending order.
# For example, if the input is [5, 2, 9, 1, 5], the output should be [1, 2, 5, 5, 9].
def sort_array(int_arr):
    return sorted(int_arr)


def test_sort_array():
    assert sort_array([5, 2, 9, 1, 5]) == [1, 2, 5, 5, 9]
    assert sort_array([5, 2, 9, 1, 5, 0]) == [0, 1, 2, 5, 5, 9]
    assert sort_array([5, 2, 9, 1, 5, 0, 0]) == [0, 0, 1, 2, 5, 5, 9]


# Write a Python function to calculate the factorial of a number recursively.
def calculate_factorial_recursive(num):
    if num == 0:
        return 1
    return num * calculate_factorial_recursive(num - 1)
    # another solution
    # return math.factorial(num)


def test_calculate_factorial_recursive():
    assert calculate_factorial_recursive(0) == 1
    assert calculate_factorial_recursive(3) == 6
    assert calculate_factorial_recursive(5) == 120


# Given a string, write a function in Python to count the number of vowels in the string.
def count_vowels_in_string(str):
    vowels = 'aeiou'
    count = 0
    for char in str:
        if char in vowels:
            count += 1
    return count


def test_count_vowels_in_string():
    assert count_vowels_in_string('hello') == 2
    assert count_vowels_in_string('hello world') == 3
    assert count_vowels_in_string('hello world aa!') == 5


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def reverse_linked_list(head):
        prev_node = None
        current_node = head
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        return prev_node


def test_a():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    reversed_head = Node.reverse_linked_list(head)
    current_node = reversed_head
    while current_node:
        print(current_node.data)
        current_node = current_node.next


# check if two strings are anagrams of each other
def check_two_strings_are_anagrams(string1, string2):
    if len(string1) != len(string2):
        return False
    if set(string1) != set(string2):
        return False
    return True


def test_check():
    assert check_two_strings_are_anagrams('abc', 'bca') is True
    assert check_two_strings_are_anagrams('cinema', 'iceman') is True
    assert check_two_strings_are_anagrams('hello', 'world') is False
    assert check_two_strings_are_anagrams('hello', 'lloeh') is True


# Given a sorted array of integers, write a function in Python \n
# to find the index of a target value using binary search.
def find_sorted_array_value_index(int_array, value):
    for i in range(len(int_array)):
        if int_array[i] == value:
            return i
    return -1


def test_find_sorted_array_value_index():
    assert find_sorted_array_value_index([1, 2, 3, 4, 5], 3) == 2
    assert find_sorted_array_value_index([1, 2, 3, 4, 5], -1) == -1
    assert find_sorted_array_value_index([1, 2, 3, 4, 5], 6) == -1
    assert find_sorted_array_value_index([1, 2, 3, 4, 5], 0) == -1


# Implement a function in Python to generate Fibonacci series up to a given number.
def generate_fibonacci_list(number):
    if number == 0:
        return [0]
    if number == 1:
        return [0, 1]
    if number == 2:
        return [0, 1, 1]
    if number > 2:
        fib_list = [0, 1, 1]
        for i in range(2, number):
            fib_list.append(fib_list[i] + fib_list[i - 1])
        return fib_list


def test_generate():
    assert generate_fibonacci_list(0) == [0]
    assert generate_fibonacci_list(1) == [0, 1]
    assert generate_fibonacci_list(2) == [0, 1, 1]
    assert generate_fibonacci_list(3) == [0, 1, 1, 2]
    assert generate_fibonacci_list(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


# Write a Python function to find the intersection of two arrays.
def find(array1, array2):
    array1.sort()
    array2.sort()
    inter_array = []
    for i in array1:
        if i in array2:
            inter_array.append(i)
    return inter_array


def test_find():
    assert find([1, 2, 3], [2, 3, 4]) == [2, 3]
    assert find([1, 2, 2, 1], [2, 2]) == [2, 2]
    assert find([1, 2, 3], [4, 5, 6]) == []
    assert find([1, 2, 3], [1, 2, 3]) == [1, 2, 3]
    assert find([1, 2, 3], [3, 2, 1]) == [1, 2, 3]
    assert find(["a", "ab", "abc"], ["d", "ad", "b", "a"]) == ["a"]
    assert find(["a", "1", "abc"], ["d", "ad", "b", "a", "1"]) == ["1", "a"]


# Given a binary tree, write a function in Python \n
# to perform an inorder traversal and return the result as a list.
# For example, given the following binary tree:
#     1
#    / \
#   2   3
#  / \
# 4   5
# The inorder traversal would return [4, 2, 5, 1, 3].
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def inorder_traversal(self, root):
        result = []
        if root:
            result = self.inorder_traversal(root.left)
            result.append(root.value)
            result = result + self.inorder_traversal(root.right)
        return result


def test_inorder_traversal():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    assert root.inorder_traversal(root) == [4, 2, 5, 1, 3]
