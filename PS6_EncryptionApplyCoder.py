#EncryptionApplyCoder.py
def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.
    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    encodedT = ''
    # For each letter in the text change it for its couple in the coder.
    for pos in range(len(text)):
        letter = text[pos]
        encodedT += coder.get(letter,letter)
        
    return encodedT
