def isVowel2(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    
    return char.lower() in 'aeiou'

z=isVowel2('a')
print z