def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    letters = getFrequencyDict(word)

    for c in letters:
        if letters[c] > hand.get(c, 0):
            return False

    return word in wordList