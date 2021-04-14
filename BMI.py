# Caclulating BMI (unfortunatly)
# Author Enda Lynch
#REF: https://www.w3resource.com/python-exercises/python-basic-exercise-66.php
#REF: https://www.includehelp.com/python/bmi-body-mass-index-calculator.aspx
#REF: https://www.w3schools.com/python/ref_func_round.asp


# Input weight (kg) and height (cm)
Weight = float (input('Enter Weight in kg: '))   
Height = float (input('Enter height in cm: '))                                      
Height2 = (float(Height/100)**2)                        # Calculate hight in meters squared
BMI = round((Weight/Height2), 2)                        # Calculate BMI to 2 decimal places
print ('Your BMI is: {}\nPlease do not put too much stock in BMI' .format (BMI))                 # Display BMI
