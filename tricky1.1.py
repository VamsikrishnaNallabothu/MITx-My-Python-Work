iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
    print "Iteration " + str(iteration) + "; count is: " + str(count)
    iteration += 1
    #count for iteration 0,1,2,3,4