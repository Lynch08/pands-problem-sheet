# Pands-Problem-Sheet 
### Introduction
This respository contains my solutions to the Problem Set 2021 for the module Programming and Scripting, part of the Data Analytics course at GMIT.
I am a novice at programming, however it is becomeing more of a requirement in my professional life that I at least learn to do some simple automation and be a little stronger at data analysis and visual representation using computing tools more powerful than excel. Python being an introductory module in this data analyitics course was a major factor in me choosing GMITs programme.
I will say, as frustrating as some of these tasks were at times, the satisfaction in seeing my code work at the end was always a good incentive and motivator to come back for more.
# Problem Sheet for Programming and Scripting 2021
##### Requirements to run this code
An application/tool that will allow you to run Python3 (This code was written and tested using Visual Studio Code).
You could also run on a tool like cmder or idle.

# Task 1 (Wk2)
## BMI.py 
### Calculates a persons Body Mass Index using the inputs of height in cm and weight in Kg

## Code:
```py
Weight = float (input('Enter Weight in kg: '))   
Height = float (input('Enter height in cm: '))                                      
Height2 = (float(Height/100)**2)                        
BMI = round((Weight/Height2), 2)                        
print ('Your BMI is: {}\nPlease do not put too much stock in BMI' .format (BMI))
```

## Explaining the code:
###### Assign weight and heights as floating points - this is becase even if you enter the weight and height as integers there is a good chance they will become decimals after the Calculation   
###### Calculate the BMI using weight/height (meters squared)
###### Round to two decimal places so output will be clean
###### Display BMI using print function

## Refrences 
###### Credit: https://www.w3resource.com/python-exercises/python-basic-exercise-66.php (last accessed 14/04/2021)
###### Credit: https://www.includehelp.com/python/bmi-body-mass-index-calculator.aspx (last accessed 14/04/2021)
###### Credit: https://www.w3schools.com/python/ref_func_round.asp (last accessed 14/04/2021)

# Task 2 (Wk3)
## secondstring.py 
### Write a program that takes asks a user to input a string and outputs every second letter in reverse order

## Code:
```py
string = input('Please enter a sentance:')
print(string [::-2])
```

## Explaining the code:
###### Input string
###### Reverse string and output every second letter using slicing

## Refrences
###### Credit: https://www.w3schools.com/python/gloss_python_string_slice.asp (last accessed 14/04/2021)
###### Credit: Picture in Course Header :)

# Task 3 (Wk4)
## Weekday.py 
### Tells the user if it is a weekday or the weekend

## Code:
```py
import datetime

daynum = datetime.datetime.today().weekday()

if daynum < 4:                                          
    print ("Yes, unfortunately today is a weekday")
elif daynum == 4:                                       
    print('still a weekday - but its Friday - weekend is coming :)')
else:                                                   
    print ("Weekend - YEAH!!")
```
## Explaining the code:
###### Import datetime module
###### Use datetime to "get" .today and .weekday to return the day of the week in numerical form, 0-6 : Mon-Sun
###### use if, elif and else to determine output
###### Tell if it is a weekend or weekday

## Refrences 
###### Credit: https://stackoverflow.com/questions/29384696/how-to-find-current-day-is-weekday-or-weekends-in-python (last accessed 14/04/2021)
###### Credit: https://www.w3schools.com/python/python_conditions.asp (last accessed 14/04/2021)
###### Credit: https://realpython.com/python-conditional-statements/ (last accessed 14/04/2021)

# Task4 (Wk5)
## collatz.py
### Programme to input a number, if even divide by 2 if odd multiply by 3 and add 1. Finsh when value is 1

## Code:
```py
inNum = int(input("Please enter a number: "))   
numbers = []                                    
numbers.append(inNum)                          

while inNum != 1:                               
    if (inNum % 2) == 0:                        
       inNum = (inNum / 2)                      
       numbers.append(int(inNum))              
    else:                           
        inNum = (inNum * 3 + 1)                
        numbers.append(int(inNum))              
        
print (numbers) 
```
## Explaining the code:
###### Input your number
###### Create empty list
###### Start loop - as long as the input number is not 1 keep going
###### If even divide by 2
###### If odd multiply by 3 and add 1
###### Append number to list every time (this is the .append in 3rd line of code)
###### Print full list when loop reaches end(1)

## Refrences 
###### Credit: https://www.w3schools.com/python/python_while_loops.asp (last accessed 14/04/2021)
###### Credit: https://realpython.com/python-while-loop/ (last accessed 14/04/2021)
###### Credit: https://realpython.com/python-append/ (last accessed 14/04/2021)
###### Credit: Sweigart, A. (2005). Automate the boring stuff with python. In Decision Support Systems. Pages 45 - 50

# Task 5 (Wk6)
## squareroot.py and squareroot2.py
### A programme so when you input a number it will return the square root using Newtons method using a function
##### Note: I added a second way of doing this task that that would loop to precision as per feedback - and added error handling

## Code for loop to set amount of iterations:
```py
newt = input("Number to get square root of:" )

def sqrt(number, iterations = 100):
    newt = float(number) 
    for i in range(1, iterations): 
        number = 0.5 * (newt / number + number)
    return round((number), 1)

print ("Square number of", newt, "is approx:", (sqrt(float(newt))))

```
## Explaining the code:
###### Input number = newt
###### Create function 'sqrt' that uses a 'for' loop through a set amount of iterations of newtons method - √ number ≈ .5*(a/number + number)) using the input number(changed to float)
###### Number needs to be returned and used in the next iteration
###### Round to 1 decimal place
###### Output aprox square root(float)

## Code for loop to percision:
```py

num = 1.0
babr = 1.0                                      
num = input("Please enter a positive number: ")

def sqrt(num):
    try:
        num = float(num)
        if num >= 0.0:                                   
            babr = num / 2                                   
            while abs(babr - (num / babr)) > 0.01:       
                babr = (babr + (num / babr)) * .5
            babr = round(babr,1)                         

            print("The square root of", num, "is approx.", babr)
        else:
            print(num, "is not a positive number.")      

    except:
        print(num, "is not a number.")                   

sqrt(num)
```
## Explaining the code:
###### Input number = num
###### Create function 'sqrt' that uses error handling to ensure a positive float/integer has been input.
###### Use while loop to iterate to precision to .01 - using the abs() function (absolute value)
###### Round to 1 decimal place
###### Output aprox square root(float) - if negative num or other characters are entered show error 

## Refrences 
###### Credit: https://medium.com/@sddkal/newton-square-root-method-in-python-270853e9185d (last accessed 14/04/2021)
###### Credit: https://www.youtube.com/watch?v=WsQQvHm4lSw - Understand Calculas (last accessed 14/04/2021)
###### Credit: https://www.homeschoolmath.net/teaching/square-root-algorithm.php (last accessed 14/04/2021)
###### Credit: https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/  (last accessed 14/04/2021)
###### Credit: https://www.school-for-champions.com/algebra/square_root_approx.htm#.YD102-j7TDe  (last accessed 14/04/2021)
###### Credit: Sweigart, A. (2005). Automate the boring stuff with python. In Decision Support Systems. Pages 61 - 77
###### Credit: https://blogs.sas.com/content/iml/2016/05/16/babylonian-square-roots.html (last accessed 14/04/2021)
###### Credit: Error handling video from Topic 9, Andrew Beatty.
###### Credit: https://realpython.com/python-exceptions/  (last accessed 14/04/2021)

# Task 6 (Wk7)
## es.py 
## Programme to count the amount of " e's " in a text file - (using moby-dick.txt) from argument in command line

## Code:
```py
import sys
filename = sys.argv[1]

def readLetter(filename, letter):
    try:                                            
        with open (filename) as f:                  
            txt = f.read()                          
            count = 0                               
            for lett in txt:                        
                if lett == letter:
                    count += 1                      
            return count                            
    except FileNotFoundError:                       
        print ("That file (", filename, ") does not exist", sep='')
                     

print(readLetter(filename, 'e'))                               
```
## Explaining the code:
###### Import sys to read argument from command line
###### Create function "readLetter" to read file
###### Open and Read file using .read
###### Use 'For' Loop to add +1 to count every time designated character is found (count needs to be returned every time)
###### Print final count
###### Use '.\TxtFiles\moby-dick.txt' in command line to return count - textfiles are stored in seperate folder
###### Added error handeling in the case that the file entered to the commandline does not exist

## Refrences 
###### Credit: https://stackoverflow.com/questions/14360389/getting-file-path-from-command-line-argument-in-python/47324233 (last accessed 14/04/2021)
###### Credit: https://realpython.com/python-command-line-arguments/ (last accessed 14/04/2021)
###### Credit:https://www.pythontutorial.net/python-basics/python-read-text-file/ (last accessed 14/04/2021)
###### Credit:https://www.geeksforgeeks.org/reading-writing-text-files-python/ (last accessed 14/04/2021)
###### Credit:https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/ (last accessed 14/04/2021)
###### Credit: http://bioinf.gen.tcd.ie/pol/moby.dick.txt (last accessed 14/04/2021)
###### Credit: Error handling video from Topic 9, Andrew Beatty.
###### Credit: https://realpython.com/python-exceptions/ (last accessed 14/04/2021)

# Task 7 (Wk8)
## plotTask.py 
### A program that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes

## Code:
```py
import numpy as np 
import matplotlib.pyplot as plt 

x = np.arange(0.0, 5.0, 1.0)
y1 = x
y2 = x**2
y3 = x**3

fig = plt.figure()
fig.patch.set_facecolor('xkcd:mint green')
plt.rcParams['axes.facecolor'] = 'xkcd:sky blue'

plt.plot(y1, label = 'f(x)', color = 'magenta', linewidth = 2, linestyle = 'solid', marker = 'd', markersize = 7, markerfacecolor = 'gold')
plt.plot(y2, label = 'g(x)', color = 'green', linewidth = 2, linestyle = 'dotted', marker = 'd',markersize = 7, markerfacecolor = 'gold')
plt.plot(y3, label = 'h(x)', color = 'red', linewidth = 2, linestyle = 'dashed', marker = 'd', markersize = 7, markerfacecolor = 'gold')

plt.title('Wk8 Lab: f(x)=x, g(x)=x**2 and h(x)=x**3', fontweight = 'bold', fontsize = 14)
plt.xlabel('x-axis', fontweight = 'bold', fontsize = 12)
plt.ylabel('y-axis', fontweight = 'bold', fontsize = 12)
plt.legend()
plt.show() #plt.savfig() when required
```
## Explaining the code:
###### Import libaries numpy (to create a range of the data) and matplotlib.pyplot (to plot and visualise the data)
###### Use the arange() function (takes four parameters that includes start, stop, step, and dtype and returns evenly spaced values within a given interval) to set parameters of plot
###### Create y1, y2 and y3 to as  x, x**2, and x**3 respectivly
###### plt.plot plots the points and allows formatting of the lines by colour, style and width, and formattting of the plot points by shape, colour and size
###### Use plt.title to set a title and format font
###### Use plt.xlabel and plt.ylabel to label x-axis and y-axis and format font
###### Generate plotted image using plt.show() and save using plt.savfig() when finished

![plotTask Wk08](https://user-images.githubusercontent.com/77644253/111052116-2e104380-8450-11eb-9cb9-b9c0c106692b.PNG)

## Refrences 
###### Credit: https://realpython.com/how-to-use-numpy-arange/ (last accessed 14/04/2021)
###### Credit: https://stackoverflow.com/questions/14088687/how-to-change-plot-background-color (last accessed 14/04/2021)
###### Credit: https://stackoverflow.com/questions/18962063/matplotlib-setting-title-bold-while-using-times-new-roman (last accessed 14/04/2021)
###### Credit: https://www.programcreek.com/python/example/4890/matplotlib.rcParams (last accessed 14/04/2021)
