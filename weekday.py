#Programme that will let user know if it is a weekday or weekend
#Author: Enda Lynch
import datetime

daynum = datetime.datetime.today().weekday()

if daynum < 5:                                          # 0-4 is Mon-Fri
    print ("Yes, unfortunately today is a weekday")
else:                                                   # 5 Sat, 6 Sun
    print ("Weekend - YEAH!!")