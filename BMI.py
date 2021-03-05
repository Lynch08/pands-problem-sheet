# Caclulating BMI (unfortunatly)
# Author Enda Lynch


# Input weight (kg) and height (cm)
Weight = float (input('Enter Weight in kg: '))   
Height = float (input('Enter height in cm: '))                                      
Height2 = (float(Height/100)**2)                        # Calculate hight in meters squared
BMI = round((Weight/Height2), 2)                        # Calculate BMI to 2 decimal places
print ('Your BMI is: {}' .format (BMI))                 # Display BMI
