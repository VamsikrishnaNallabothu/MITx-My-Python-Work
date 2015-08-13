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
