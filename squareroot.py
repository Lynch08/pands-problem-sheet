#Programme so when you input a number it will return the square root
#Author Enda Lynch
#REF https://medium.com/@sddkal/newton-square-root-method-in-python-270853e9185d
#REF https://www.youtube.com/watch?v=WsQQvHm4lSw - Understand Calculas
#REF https://www.homeschoolmath.net/teaching/square-root-algorithm.php
#REF https://www.goeduhub.com/3398/python-program-to-find-the-square-root-number-newtons-method


a = input("Number to get square root of:" )

def sqrt(number, number_iters = 1000):
    a = float(number) # number to get square root of
    for i in range(number_iters): # iteration number
        number = 0.5 * (number + a / number) 
	  # x_(n+1) = 0.5 * (x_n +a / x_n)
    return float(number)

print ("Square number of", a, "is approx:", (sqrt(float(a))))
