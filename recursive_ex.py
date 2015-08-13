#adding a- b times or multiplying a with b
def recurMUL(a,b):
    if b==1:
      return a
    else:
        return a+ recurMUL(a,b-1)

def recurFact(n):
    if n==1:
        return 1
    else:
        return n*recurFact(n-1)
def recurPower(base, exp):
    if exp==0:
        return float(1)
    else:
        return float(base) * recurPower(base, exp-1)

def recurPowerNew(base, exp):
    if (exp>0 and exp%2==0):
        return recurPowerNew(base*base, exp/2)
    elif(exp>0 and exp%2!=0):
        return base*recurPowerNew(base, exp-1)
    elif(exp==0):
        return float(1)
        
    



    