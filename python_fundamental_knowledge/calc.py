on = True


def add():
    a = float(input("Enter a number: "))
    b = float(input("Enter another number: "))
    print(a + b)


def subtract():
    a = float(input("Enter a number: "))
    b = float(input("Enter another number: "))
    print(a - b)


def multiply():
    a = float(input("Enter a number: "))
    b = float(input("Enter another number: "))
    print(a * b)


def divide():
    a = float(input("Enter a number: "))
    b = float(input("Enter another number: "))
    print(a / b)


while on:
    operation = input("Please choose +, -, *, /, or q")
    if operation == '+':
        add()
    elif operation == '-':
        subtract()
    elif operation == '*':
        multiply()
    elif operation == '/':
        divide()
    elif operation == 'q':
        on = False
    else:
        print("That operation is not available.")
