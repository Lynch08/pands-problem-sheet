


inNum = int(input("Please enter a number: "))
numbers = []
numbers.append(inNum)


while inNum != 1:
    if (inNum % 2) == 0:
       numbers.append(inNum / 2)
       inNum = inNum / 2
    else:
        numbers.append(inNum * 3 + 1)
        inNum = inNum * 3 + 1
        
  
print numbers.append(inNum)