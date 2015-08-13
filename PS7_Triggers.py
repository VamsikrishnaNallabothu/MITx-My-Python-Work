#PS7_Triggers.py
# Enter your code for WordTrigger, TitleTrigger, 
# SubjectTrigger, and SummaryTrigger in this box
class Trigger(object):
    """
    A trigger is a rule that is evaluated over a single news story 
    and may fire to generate an alert.
    """
    
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError

# Whole Word Triggers.
# Problems 2-5.
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
