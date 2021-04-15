#reading all the e's from a text file using argument in command line
#Text file kept in seperate folder so use 'python es.py .\TxtFiles\moby-dick.txt' in command line to return count
#Author Enda Lynch
#REF: https://stackoverflow.com/questions/14360389/getting-file-path-from-command-line-argument-in-python/47324233
#REF: https://realpython.com/python-command-line-arguments/
#REF: https://www.pythontutorial.net/python-basics/python-read-text-file/
#REF: https://www.geeksforgeeks.org/reading-writing-text-files-python/
#REF: https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/
#REF: http://bioinf.gen.tcd.ie/pol/moby.dick.txt
#REF: Error handeling video from Topic 9, Andrew Beatty.
#REF: https://realpython.com/python-exceptions/ 

import sys
filename = sys.argv[1]

def readLetter(filename, letter):
    try:                                            #create function to read file
        with open (filename) as f:                  # open file
            txt = f.read()                          #read file
            count = 0                               #count begins at:0
            for lett in txt:                        #loop for char
                if lett == letter:
                    count += 1                      #+1 every time char is found
            return count                            #return number of characters
    except FileNotFoundError:                       #Error handeling if file does not exist
        print ("That file (", filename, ") does not exist", sep='')
                     

print(readLetter(filename, 'e'))                    # use 'python es.py .\TxtFiles\moby-dick.txt' in command line to return count