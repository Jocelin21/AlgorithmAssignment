"""
Create a function that can check if a prime also has an emirp (the prime number but reversed).
An example would be the number 13 as its reverse, 31, is also a prime number. Another example 
would be the number 347 as its reverse, 743, is also a prime number.
The function returns the boolean True and prints both the number and the emirp if the number 
passed in is a prime and also has an emirp. Otherwise, return False and print "False!".
Sample input and output:
emirpCheck(13)
# Output -> 13 31
emirpCheck(347)
# Output -> 347 743
emirpCheck(5)
# Output -> False!
"""
number = int(input("Enter a number: "))
numbers = number
#Prime Number
def prime(number):
    for i in range(2, number - 1):
        if number % i == 0:
            return False
    return True

#For emirp
def emirpCheck(number):
    if prime(number) == False or number < 12:
        print("False!")
    else:
        x = 0  
        while (number > 0):  
            remainder = number % 10  
            x = (x * 10) + remainder  
            number = number // 10  
        if x == prime(number) == False:
            print("False!")
        else:
            print(numbers, x)

emirpCheck(number)