import re       #use regex for overlapping occurances
s = 'azcbobobegghakl'
def isBob(s):
    return len(re.findall('(?=bob)', s))
z=isBob(s)
print 'Number of times bob occurs is: ' , z

#Assume s is a string of lower case characters.

#Write a program that prints the number of times the string 'bob' occurs in s.
#For example, if s = 'azcbobobegghakl', then your program should print

#Number of times bob occurs is: 2