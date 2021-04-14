#Programme so when you input a number it will return the square root
#Author Enda Lynch
#REF https://medium.com/@sddkal/newton-square-root-method-in-python-270853e9185d
#REF https://www.youtube.com/watch?v=WsQQvHm4lSw - Understand Calculas
#REF https://www.homeschoolmath.net/teaching/square-root-algorithm.php
#REF https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/
#REF https://www.school-for-champions.com/algebra/square_root_approx.htm#.YD102-j7TDe 
#REF Automate the Boring Stuff - Chapter 3 Functions
#REF https://blogs.sas.com/content/iml/2016/05/16/babylonian-square-roots.html
#REF: Error handling video from Topic 9, Andrew Beatty.
#REF: https://realpython.com/python-exceptions/ 


# initial Values
num = 1.0
babr = 1.0                                      #babylonian root
num = input("Please enter a positive number: ") # input and set num as variable

# Try to check if inputted value for 'num' is positve - Topic 9 error handling
# Calculate the approximate square root of 'num' using Babylonian square-root method
def sqrt(num):
    try:
        num = float(num)
        if num >= 0.0:                                   # If 'num' is an positive number
            babr = num / 2                               # Set first approximation of root to half of 'num'     
            while abs(babr - (num / babr)) > 0.01:       # Loop until the difference between 'babr' and 'num' divided by 'babr' gives a value less than 0.01
                babr = (babr + (num / babr)) * .5         #
            babr = round(babr,1)                         # Round babr to one decimal place

            print("The square root of", num, "is approx.", babr)
        else:
            print(num, "is not a positive number.")      # Otherwise prints a VALUE error message if 'num' is not a positive number

    except:
        print(num, "is not a number.")                   # Prints a TYPE exception error if 'num' not a number type variable

sqrt(num)