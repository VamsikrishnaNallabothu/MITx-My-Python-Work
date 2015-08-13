def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.
    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    assert (shift in range(0,26)), 'Shift value is out of range'
    
    # Generate the coder and apply it to the text.
    return applyCoder(text, buildCoder(shift))
