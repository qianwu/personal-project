fruits = ["apple","watermelon","sherbet","raspberries"]
for fruit in fruits:
    print("Would you like {} ?".format(fruit))

for number in range(1,11):
    print("Number {}".format(number))

# while loop
# temp_f = 40
# while temp_f > 32:
#     print("The temperature is {} degrees.".format(temp_f))
#     temp_f -= 1

# loop controls
# break
# end the loop .go to the next statement in the program(outside the loop)
#continue
# skips current part of the loop. moves to the next part of the loop
# pass
# skips any part of the loop where "pass" appears. best used for testing code
temp_f = 40
while temp_f > 32:
    print("The temperature is {} degrees.".format(temp_f))
    temp_f -= 1
    if temp_f == 35:
        break

for number in range(1,11):
    if number == 5:
        print("We're skipping number 5")
        continue
    print("This is the number {}".format(number))

for number in range(1,11):
    if number == 3:
        pass
    else:
        print("This is the number {}".format(number))

