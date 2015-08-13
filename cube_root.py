x=int(raw_input("Enter an Integer:"))
ans=0
while (ans**3<x):
  ans=ans+1
if(ans**3)!= x:
    print(str(x) + 'is not a perfect Square')
else:
    print('cube root of' + str(x) + 'is' + str(ans)) 

#can also be modified as
# while (ans**3 !=x ):
#    ans=ans+1
# print('cube root of' + str(x) + 'is' + str(ans)) 