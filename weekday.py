#Programme that will let user know if it is a weekday or weekend
#Author: Enda Lynch
#REF: https://stackoverflow.com/questions/29384696/how-to-find-current-day-is-weekday-or-weekends-in-python
#REF: https://www.w3schools.com/python/python_conditions.asp

import datetime                                         #datetime module

daynum = datetime.datetime.today().weekday()

#using if, elif and else
if daynum < 4:                                          # 0-3 is Mon-Thurs
    print ("Yes, unfortunately today is a weekday")
elif daynum == 4:                                       # 4 is Fri
    print('still a weekday - but its Friday - weekend is coming :)')
else:                                                   # 5 Sat, 6 Sun
    print ("Weekend - YEAH!!")