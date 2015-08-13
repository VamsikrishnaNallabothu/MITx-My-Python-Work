# Lecture 3.7, slide 3

# Newton-Raphson for square root

epsilon = 0.01
y = 12345.0
guess = y/2.0

while abs(guess**2 - y) >= epsilon:
    guess = guess - (((guess**2) - y)/(2*guess)) #g= g-(g^2-y)/2*g 
    print(guess)
print('Square root of ' + str(y) + ' is about ' + str(guess))