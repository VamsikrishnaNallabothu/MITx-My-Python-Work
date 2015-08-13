#Bisection search (will find if the number is between the low and high)
#will reduce the number of guesses

x=float(raw_input('Enter the number:'))
epsilon=0.01

high=x
low=0.0
guess_num=0
ans=(low+high)/2.0
while abs(ans**2 -x)>=epsilon: #every answer will be more than 0.01
    print('low= ' +str(low) + ' high= ' +str(high)+ 'middle num : ' +str(ans) )
    guess_num+=1
    if ans**2>x: #if the (half the given num)sqrt is greater than the given number, the numbers more than 
        #the bisection value arer eliminated from the testing
        high=ans #the value of high is decreased by half of the given num and is then set to iterate in the loop
    else:
        low=ans  # if the sqrt(half the given num) is less than the given number, the 
    ans = (high + low)/2.0
print('num of guesses : ' +str(guess_num))
print('The square root of '+ str(x) + ' is ' + str(ans))