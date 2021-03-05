#Programme so when you input a number it will return the square root
#Author Enda Lynch
#REF https://medium.com/@sddkal/newton-square-root-method-in-python-270853e9185d
#REF https://www.youtube.com/watch?v=WsQQvHm4lSw - Understand Calculas
#REF https://www.homeschoolmath.net/teaching/square-root-algorithm.php
#REF https://www.goeduhub.com/3398/python-program-to-find-the-square-root-number-newtons-method
#REF https://www.school-for-champions.com/algebra/square_root_approx.htm#.YD102-j7TDe 
#REF Automate the Boring Stuff - Chapter 3 Functions


newt = input("Number to get square root of:" )

def sqrt(number, iterations = 100):
    newt = float(number) # number to get square root of
    for i in range(1, iterations): # iteration number
        number = 0.5 * (newt / number + number) # √ number ≈ .5*(newt/number + number)	  
    return round((number), 1)

print ("Square number of", newt, "is approx:", (sqrt(float(newt))))
