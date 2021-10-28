"""
Create a function that prints a statement after a given amount of time (initial lag).
The function accepts two arguments, one being the statement that's printed (str), 
and the other being the time delay (int).
Sample input and output:
delay("This is message", 5)
# Output -> This is message (PRINTED AFTER 5 SECONDS)
"""
import time    

def delay(message, second):
    time.sleep(second)
    print(message)

delay("This is message", 5)