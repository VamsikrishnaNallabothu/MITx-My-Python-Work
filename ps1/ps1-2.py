 # Paste your code into this box 
import re       #use regex for overlapping occurances
def isBob(s):
    return len(re.findall('(?=bob)', s))
z=isBob(s)
print 'Number of times bob occurs is: ' , z