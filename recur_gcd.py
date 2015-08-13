def itergcd(a,b):
    smaller = min(a,b)
    while(a%smaller!=0 or b%smaller!=0):
        smaller-=1
    return smaller
def recurgcd(a,b):
    if(b==0):
        return a
    else:
        return recurgcd(b,a%b)

