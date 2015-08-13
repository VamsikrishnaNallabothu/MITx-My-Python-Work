EncryptionBuildCoder.py
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.
    shift: 0 <= int < 26
    returns: dict
    """
    assert (shift in range(0,26)), 'Shift value is out of range'
    
    caesarDict = {}
    alphabets = [string.ascii_uppercase,string.ascii_lowercase]
    # For each alphabet and each letter of the alphabet apply the shift.
    for alph in alphabets:
        for letter in range(len(alph)):
            nLetter = letter + shift
            if (nLetter >= 26):
                # Back to the initial letters of the alphabet.
                nLetter -= 26
            caesarDict[alph[letter]] = alph[nLetter]
            
    return caesarDict       
