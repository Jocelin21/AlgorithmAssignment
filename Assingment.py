import random

randomint = random.randint (1, 100)
number = int(input("Pick a number from 1-100: "))

if number < 1 or number > 100:
    print ("Number is out of range.")
elif number == randomint:
    print ("You're correct!")
elif number > randomint:
    print ("The guess was too high.")
else:
    print ("The guess was too low.")