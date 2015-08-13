#to show that an integer is divisible ny 2 and 3
x=int (raw_input('Enter an Integer'))
if x%2==0:
 if x%3==0:
     print ('Divisible by 2 and 3')
 else:
         print ('Divisible by 2 and not divisible by 3')
elif x%3==0:
    print('Divisible by 3, not divisible by 2')
else:
     print 'not divisible by 2 and 3'
     