#Canopy
#Author: Vamsi
# Enter your code for WordTrigger, TitleTrigger,
# SubjectTrigger, SummaryTrigger, PhraseTrigger, and 
# filterStories in this box
class PhraseTrigger(Trigger):
    """
    This fires when a given phrase is in any of the 
    story's subject, title, or summary. 
    """
    
    def __init__(self,phrase):
        """
        Class's constructor.
        """
        self.phrase = phrase
    
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        return ((self.phrase in story.getSubject()) or (self.phrase in story.getTitle()) 
        or (self.phrase in story.getSummary()))


def filterStories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.
    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    validStories = []
    for story in stories:
        for trigger in triggerlist:
            if (trigger.evaluate(story)):
                validStories.append(story)
                break
 
    return validStories
class WordTrigger(Trigger):
    """
    Word trigger abstract class.
    """
    
    def __init__(self,word):
        """
        Class's constructor.
        """
        self.word = word
    
    def isWordIn(self,text):
        """
        It returns True if the whole word 'word' is present 
        in 'text', False otherwise. 
        """
        # Replaces every punctuation mark in text with a space.
        text = text.lower()
        for char in string.punctuation:
            text = text.replace(char,' ')
        # Break up the text into a list of distinct words.
        wordsL = text.split(' ')
        # Search word into words list.
        if self.word.lower() in wordsL:
            return True
        else:
            return False
        
class TitleTrigger(WordTrigger):
    """
    This trigger fires when a news item's title contains a given word. 
    """
    
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        return WordTrigger.isWordIn(self,story.getTitle())

class SubjectTrigger(WordTrigger):
    """
    This trigger fires when a news item's subject contains a given word. 
    """
    
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        return WordTrigger.isWordIn(self,story.getSubject())

class SummaryTrigger(WordTrigger):
    """
    This trigger fires when a news item's summary contains a given word. 
    """
    
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        return WordTrigger.isWordIn(self,story.getSummary())
