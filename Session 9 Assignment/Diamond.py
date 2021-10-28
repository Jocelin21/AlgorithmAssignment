"""
Create a function to create a diamond pattern. Tell the user to specify the height of the diamond 
and then print the diamond pattern with that specified height.
Total height = (2 * width - 1)
Extra points if you can do with just one for loop This one needs a bit of math / pattern logic
"""
height = int(input("Enter the height: "))

def diamond(height):
    for i in range(height-1):
        print(" " * (height-1-i) + "*" * (i*2+1))
    for i in range(height):
        print(" " * i + "*" * (((height-i)*2)-1))

diamond(height)


    
