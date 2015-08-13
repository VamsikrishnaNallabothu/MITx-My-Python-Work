def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Use the functions getStoryString and loadWords to get the
    raw data you need.
    returns: string - story in plain text
    """
    # Load story.
    story = getStoryString()
    
    # Obtain the shift to decrypt.
    shift= findBestShift(loadWords(), story)
    
    # Decrypt the story.
    story = applyShift(story, shift)
    
    # Returns the story in plain text.
    return story
