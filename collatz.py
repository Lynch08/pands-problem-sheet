#Programme to input a number, if even divide by 2 if odd multiply by 3 and add 1
#Finsh when value is 1
#Author: Enda Lynch
#REF: https://www.w3schools.com/python/python_while_loops.asp
#REF: Sweigart, A. (2005). Automate the boring stuff with python. In Decision Support Systems. Pages 45 - 50

inNum = int(input("Please enter a number: "))   #input your number
numbers = []                                    #name your list
numbers.append(inNum)                           #append list with input number


while inNum != 1:                               #start loop - as long as the input number is not 1 keep going
    if (inNum % 2) == 0:                        #define parameter (is the number odd or even?)
       inNum = (inNum / 2)                      #if even divide by 2
       numbers.append(int(inNum))               # add to list
    else:                           
        inNum = (inNum * 3 + 1)                 #if odd multiply by 3 and add 1
        numbers.append(int(inNum))              #add to list
        
print (numbers)                                 #print full list when loop reaches end(1)