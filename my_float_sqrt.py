x= float(raw_input('Enter a float value:'))
print x
ans=0
epsilon=0.01
step=0.1
while (ans**2)<x:
       ans+=step
       print ans

if(ans**2==x):
   print ans
else:
    ans= ans-epsilon
    print str(ans) + 'success'