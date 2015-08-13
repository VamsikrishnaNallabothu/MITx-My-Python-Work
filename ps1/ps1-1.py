 # Paste your code into this box 
def isVowels(s):
  return s.count('a'), s.count('e'), s.count('i'), s.count('o'), s.count('u')

z=isVowels(s)
y=sum(z)
print'Number of vowels:', y