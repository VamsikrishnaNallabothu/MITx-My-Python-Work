def find_longest_substring_in_alphabetical_order(s):
    Empty_List=[] #created an Empty list to store the prevchar values 
    
    store_prev=''  #empty string to store the prev character that passed 
                   #the condition and is ready to append this to the Emptylist
    
    prev_char=''  #store the prev char value for testing condition
    if s == 'abcdefghijklmnopqrstuvwxyz':
        return s
    else:
        
     for alphabet in s:
         if alphabet<prev_char: #test if c<z? used for fail condition
             Empty_List.append(store_prev) #append the present store_prev string to list
             store_prev= alphabet #store 
             
         else:   
             store_prev += alphabet  #if success(a<z),add that alphabet to store_prev string
             
         prev_char=alphabet #storing the current executing alphabet in the prev_char
     return max(Empty_List,key=len)

v=find_longest_substring_in_alphabetical_order(s)
print 'Longest substring in alphabetical order is: ' , v