print 'Please think of a number between 0 and 100!'
low=0
high=100
guess= False
while not guess:
   secret_num=(high+low)/2
   print 'Is your secret number '+ str(secret_num)+ '?'
   x=raw_input("Enter ' h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low.Enter 'c' to indicate I guessed correctly:")
   
   if(x=='h'):
    high=secret_num
    secret_num=(high+low)/2
  
   elif(x=='l'):
    low =secret_num
    secret_num=(high+low)/2
   
   elif(x=='c'):
    print 'Game over. Your secret number was: ' + str(secret_num)
    break
   else:
      print 'I did not understand your input'
   secret_num=(high+low)/2   