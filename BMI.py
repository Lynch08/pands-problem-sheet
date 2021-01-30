# Caclulating BMI (unfortunatly)
# Author Enda Lynch


# Input weight (kg) and height (cm)
Weight = float (input('Enter Weight in kg: '))   
Height = float (input('Enter height in cm: '))   

# Calculate hight in meters squared
Height2 = (float(Height/100)**2)

# Calculate BMI to 2 decimal places
BMI = round((Weight/Height2), 2)

# Display BMI
print ('Your BMI is: {}' .format (BMI))
