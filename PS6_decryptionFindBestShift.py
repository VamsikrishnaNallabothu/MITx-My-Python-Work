def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.
    text: string
    returns: 0 <= int < 26
    """
    # Set the maximum number of real words found and the best shift to 0.
    maxRealW = 0
    bestShift = 0
    
    # For each possible shift from 0 to 26.
    for shift in range(26):
    	# Shift the entire text and split the text up into a list of the individual words.
    	sText = applyShift(text, shift).split(' ')
    	# Count the number of valid words in this list.
    	countRW = 0
    	for word in sText:
    		if (isWord(wordList, word)):
    			countRW += 1
    	# If the number of valid words is more than the largest number of real words found:
    	if (countRW > maxRealW):
    		# Record the number of valid words and set the best shift to the current shift.
	    	maxRealW = countRW
	    	bestShift = shift

    # Return the best shift.
    return bestShift