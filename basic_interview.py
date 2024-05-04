# swap two variables 
# 1. using a temporary variable
a = 1
b = 2
temp = a
a = b
b = temp
print(a,b)
# 2. without using a temporary variable
a = 1   
b = 2   
a,b = b,a
print(a,b)
# 3. using arithmetic operations
a = 1
b = 2
a = a + b
b = a - b
a = a - b
print(a,b)

# check for prime number
def is_prime(n):
    # check if n is less than 2
    if n < 2:
        return False
    #check for factors from 2 to the square root of n
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
print(is_prime(7))
print(is_prime(10))

# generate random number float between 0 and 1
import random
num = random.random()
print(num)

#give a random float number in a range
num = random.uniform(1,10)
print(num)

#give a random integer number in a range
num = random.randint(1,10)
print(num)

# gives a random number in a range with incremental steps
num = random.randrange(0,101,5) #generate a random number between 0 and 100 ,but only multiples of 5
print(num)

# give a series of random numbers
numerlist = random.sample(range(1,100),5) #generate 5 random numbers between 1 and 100
print(numerlist)

# print fibonacci series
def print_fibonacci_series(n):
    a,b = 0,1
    print(a,end=" ")
    if n> 1:
        print(b,end=" ")
    for _ in range(2,n):
        c = a + b
        print(c,end=" ")
        a,b = b,c
        
print_fibonacci_series(10)