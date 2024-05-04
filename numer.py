import decimal
# decimal attention
def subtract(a,b):
    return a-b
print(subtract(5,2)) #3
print(subtract(1.2,1.0))  #0.19999999999999996
print(subtract(decimal.Decimal('1.2'),decimal.Decimal('1.0')))  #0.2

# the power of number
def power(a,b):
    return a**b
print(power(2,3)) #8 means 2*2*2