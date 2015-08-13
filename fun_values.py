def f(x):
    #x=1, if we give this, z would print out 2 as the value of y is already is defined in the function
     y=1
     x=x+y
     return x
    
x=2
y=2
z=f(x)
print z
print y