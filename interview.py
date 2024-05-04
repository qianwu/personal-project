# variables are dynamicly typed
n = 0
print('n = ', n)

# multiple assignment
n,m = 0,"abc"

n,m,z = 0.125,"abc", False
print('n = ', n)

# Increment and Decrement
n = n+1 #good
n +=1 #better
n -=1 #better
#n++ #not allowed

#None is null
n = 4
n = None
print('n = ', n)

# If statement don't need parenthesis
# or curly braces
n = 1
if n>2:
    n -= 1
elif n==2:
    n *= 2

# Parenthese needed for multiple conditions
# and = &&
# or = ||
n,m = 1,2
if((n>2 and n !=m) or n==m):
    n +=1

# While loops are similar to other languages
n =0 
while n<5:
    n += 1

#Looping from i=0 to i = 4
for i in range(5):
    print(i)

#Looping from i=2 to i = 4
for i in range(2,5):
    print(i)

# Looping from i = 5 to i = 2
for i in range(5,1,-1):
    print(i)

#division is decimal by default
print(5/2)

#Double slash rounds down
print(5//2)

#careful: most languages round towards 0 by
# default so negative numbers round down
print(-5//2)

# a workaround for rounding towards zero is to
# use decimal division and then convert to int.
print(int(-5/2))

# Modding is similar to most languages
print(10%3)

# except for negative values
print(-10%3)

# to be consistent with other languages modulo
import math
print(math.fmod(-10,3))

# more math helpers
print("more math helpers************")
print (math.floor(3/2)) #round down to 1
print (math.ceil(3/2)) #round up to 2
print (math.pow(2,3)) #2^3 = 8
print (math.sqrt(2)) #square root of 2

# Max / Min Int
float("inf")
float("-inf")

# python numbers are infinite so they never overflow
print(math.pow(2,1000))

#But still less than infinity
print(math.pow(2,1000) < float("inf"))

#Arrays (called lists in python)
arr = [1,2,3,4,5]
print(arr)

# can be used as a stack
arr.append(6)
print(arr)

arr.pop()
print(arr)

arr.insert(2,0)
print(arr)

arr[0] = 10
arr[1] = 20
print(arr)

# Initialize an array of size n with default value of 1
print("Initialize an array of size n with default value of 1")
n = 5 
arr = [1]*n
print(arr)
print(len(arr))

# Careful: -1 is not out of bounds
# it's the last value
print("Careful: -1 is not out of bounds")
arr = [1,2,3]
print(arr[-1]) #3

#Indexing -2 is the second to last value, etc.
print("Indexing -2 is the second to last value, etc.")
print(arr[-2]) #2

#sublists(aka slices) are also easy
print("sublists(aka slices) are also easy")
arr = [1,2,3,4,5]
print(arr[1:3]) #[2,3]

# Similar to for-loop ranges, last index is non-inclusive
print("Similar to for-loop ranges, last index is non-inclusive")
print(arr[0:4]) #[1,2,3,4]

# unpacking
a, b , c = [1,2,3]
print(a,b,c)

# be careful though
nums = [1,2,3]

#using index
for i in range(len(nums)):
    print(nums[i]) #1,2,3

# without index
for n in nums:
    print(n) #1,2,3

#with index and value
for i,n in enumerate(nums):
    print(i,n)  #0 1, 1 2, 2 3

# Loop through multiple arrays simultaneously
# with unpacking
print("Loop through multiple arrays simultaneously")
nums1 = [1,3,5]
nums2 = [2,4,6]
for n1,n2 in zip(nums1,nums2):
    print(n1,n2) #1 2, 3 4, 5 6

# Reverse an array
print("Reverse an array************")
nums = [1,2,3]
nums.reverse()
print(nums) #[3,2,1]

#sorting
print("sorting************")
arr = [5,4,7,3,8]
arr.sort()
print(arr) #[3,4,5,7,8]

arr.sort(reverse=True)
print(arr) #[8,7,5,4,3]

arr = ["bob","alice","jane","doe"]
arr.sort()
print(arr) # ['alice', 'bob', 'doe', 'jane']

# custom sorting(by length of string)
arr.sort(key= lambda x: len(x))
print(arr) # ['bob', 'jane', 'alice', 'doe']

#List comprehension
arr = [i for i in range(5)]
print(arr) #[0,1,2,3,4]

arr = [i+i for i in range(5)]
print(arr) #[0,2,4,6,8]

# 2_D lists
arr = [[0]*4 for i in range(4)]
print(arr) # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

# This won't work
arr = [[0]*4]*4
print(arr) # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

# Strings are similar to arrays
s = "abc"
print(s[0:2]) #ab
# But they are immutable
# s[0] = "A" is not allowed

# so this creates a new string
s+= "def"
print(s) #abcdef

#valid numeric stings can be converted to numbers
print(int("42")+int("43")) #85

# And numbers can be converted to strings
print(str(42)+str(43)) #4243

# In rare cases, you may need the ASCII value of a character
print(ord("a")) #97
print(ord("b")) #98

#Combine a list of Strings (with an empty string delimiter)
strings = ["ab","cd","ef"]
print("".join(strings)) #abcdef

#Queues (double ended queues)
from collections import deque
queue = deque()
queue.append(1)
queue.append(2)
print(queue) #deque([1, 2])
queue.popleft()
print(queue) #deque([2])
queue.appendleft(3)
print(queue) #deque([3, 2])
queue.pop()
print(queue) #deque([3])

#HashSets
mySet = set()
mySet.add(1)
mySet.add(2)
print(mySet) #{1,2}
print (len(mySet)) #2
print(1 in mySet) #True
print(3 in mySet) #False
mySet.remove(1)
print(1 in mySet) #False

# list to set
print (set([1,2,3])) #{1,2,3}

#set comprehension
mySet = {i for i in range(5)}
print(mySet) #{0,1,2,3,4}

#Hashmap (aka dictionary)
myMap = {}
myMap["a"] = 1
myMap["b"] = 2
print(myMap) #{'a': 1, 'b': 2}
print(len(myMap)) #2

myMap["a"] = 3
print(myMap["a"]) #3

print("a" in myMap) #True
myMap.pop("a")
print("a" in myMap) #False

myMap = {"a":10, "b":2}
print(myMap) #{'a': 10, 'b': 2}

#Dictionary comprehension
myMap = {i:2*i for i in range(3)}
print(myMap) #{0: 0, 1: 2, 2: 4}

#Loop through maps
myMap = {"a":1, "b":2}
for key in myMap:
    print(key,myMap[key]) #a 1, b 2

for val in myMap.values():
    print(val) #1,2

for key,val in myMap.items():
     print(key,val) #a 1, b 2

#Tuples are like lists but immutable
tup = (1,2,3)
print(tup) #(1,2,3)
print(tup[0]) #1
print(tup[1]) #2

#can't modify
#tup[0] = 10 #not allowed

# can be used as keys in hashmaps or sets
myMap = {(1,2):3}
print(myMap[(1,2)]) #3

mySet = set()
mySet.add((1,2))
print((1,2) in mySet) #True

#Lists can't be keys
#myMap[[3,4]] = 5 #not allowed

#Heaps
import heapq

#under the hood are arrays
minHeap = []
heapq.heappush(minHeap,5)
heapq.heappush(minHeap,2)
heapq.heappush(minHeap,3)

#Min is always at index 0
print(minHeap[0]) #2

while len(minHeap):
    print(heapq.heappop(minHeap)) #2,3,5

#No max heaps by default, workaround is to negate values
# to use min heap and multiply by -1 when you pop & push
maxHeap = []
heapq.heappush(maxHeap,-5)
heapq.heappush(maxHeap,-2)
heapq.heappush(maxHeap,-3)
#Max is always at index 0
print(-1*maxHeap[0]) #5

while len(maxHeap):
    print(-1*heapq.heappop(maxHeap)) #5,3,2

#Build heap from initial values
arr = [2,1,8,4,5]
heapq.heapify(arr)
while arr:
    print(heapq.heappop(arr)) #1,2,4,5,8

#Functions
def myFunc(n,m):
    return n *m
print(myFunc(3,4)) #12

#Nested functions have access to outer variables
def outer(a,b):
   c = "c"
   def inner():
       return a+b+c
   return inner()
print(outer("a","b")) #ab 

# can modify objects but reassign unless using nonlocal keyword
def double(arr,val):
    def helper():
        # modifying array works
        for i,n in enumerate(arr):
            arr[i] *= 2
        # will only modify val in the helper scope
        # val *= 2

        #this will modify val outside helper scope
        nonlocal val
        val *= 2
    helper()
    print(arr, val)

nums = [1,2]
val = 3
double(nums,val)

#Class
class MyClass:
    # construtor
    def __init__(self, nums):
        # create member variables
        self.nums = nums
        self.size = len(nums)

    #self key word required as parameter
    def getLength(self):
        return self.size
    def getDoubleLength(self):
        return 2 * self.getLength()
    
# Generators are like functions but use yield
print("Generators are like functions but use yield")
def count_up_to(n):
    num = 1
    while num <= n:
        yield num # This makes the function a generator
        num += 1
#using the generator
for number in count_up_to(5):
    print(number) #1,2,3,4,5

# shallow copy and deep copy
import copy
arr = [1,2,3]
arr2 = arr
arr3 = arr.copy()
arr4 = copy.deepcopy(arr)
arr[0] = 10
print(arr2) #[10,2,3]
print(arr3) #[1,2,3]
print(arr4) #[1,2,3]

# decorators are a way to modify functions
# without changing their code
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper
@my_decorator
def say_hello():
    print("Hello!")
say_hello()

# the difference between is and ==
# is checks if two variables point to the same object
# == checks if the objects pointed to have the same value
a = [1,2,3]
b = a
print(a is b) #True
