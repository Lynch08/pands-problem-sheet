# initial Values
num = 1.0
babr = 1.0
# Request user to enter a sentence and assign the value to variable 'num'
num = input("Please enter a positive number: ")

# Try to check if inputted value for 'num' is positve - Topic 9 error handling

try:
    # Try to convert 'num' to an float type
    num = float(num)
    # If 'num' is an positive number
    if num >= 0.0:
        # Set first approximation of 'root' to half of 'num'
        root = num / 2

        # Calculate the approximate square root of 'num' using Babylonian square-root
        # algorithm. Code adapted from algorithm on webpage
        # https://blogs.sas.com/content/iml/2016/05/16/babylonian-square-roots.html

        # Loop until the difference between 'root' and
        # 'num' divided by 'root' gives a value less than 0.01
        while abs(root - (num / root)) > 0.01:
            root = (root + (num / root)) / 2

        # Round root to one decimal place
        # Adapted round function code from website
        # https://stackoverflow.com/questions/13479163/round-float-to-x-decimals/22155830
        root = round(root,1)

        # Prints the result
        # Formated print code adpted from Week 7 lecture.
        print(f"The square root of {num} is approx. {root}.")
    
    # Otherwise prints a VALUE error message if 'num' is not a positive number
    else:
        print(f"Input Error: --> {num} <-- is not a positive number.")

# Prints a TYPE exception error if 'num' not a number type variable
except:
    print(f"Input Error: --> {num} <-- is not a number.")
    