def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.
    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # Keep track of the total score
    score = 0
    
    # As long as there are still letters left in the hand:
    while calculateHandlen(hand) > 0:
    
        # Display the hand
        print "Current Hand: ",
        displayHand(hand)

        # The computer chooses a word
        word = compChooseWord(hand, wordList, n)
        
        # The hand finishes when compChooseWord returns None
        if word == None:
            # End the game (break out of the loop)
            break
        else:
            word_score = getWordScore(word, n)
            score += word_score
            
            # Display word, score for that word, and the total score
            print '"' + word + '" earned', word_score, "points. Total:", \
                score, "points.\n"
                
            # Update the hand 
            hand = updateHand(hand, word)
                
    # The computer has exhausted its possible choices
    print "Total score:", score, "points."
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives
    the maximum value score, and return it.
    This word should be calculated by considering all the words
    in the wordList.
    If no words in the wordList can be made from the hand, return None.
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: string or None
    """
    # Create a new variable to store the maximum score seen so far (initially 0)
    score_max = 0
    # Create a new variable to store the best word seen so far (initially None)
    word_max = None
    # For each word in the wordList
    for word in wordList:
        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        if isValidWord(word, hand, wordList):   # TODO: optimization
            # Find out how much making that word is worth
            score = getWordScore(word, n)
            # If the score for that word is higher than your best score
            if score > score_max:
                # Update your best score, and best word accordingly
                score_max = score
                word_max = word

    # return the best word you found.
    return word_max

