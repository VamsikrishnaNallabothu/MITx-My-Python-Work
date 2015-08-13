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

# Composite Triggers
# Problems 6-8
class NotTrigger(Trigger):
    """
    This trigger should produce its output by inverting 
    the output of another trigger.
    """
    
    def __init__(self,trigger):
        """
        Class's constructor.
        """
        self.trig = trigger
    
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        return (not self.trig.evaluate(story))
    

class AndTrigger(Trigger):
    """
    This trigger should take two triggers as arguments 
    to its constructor, and should fire on a news story 
    only if both of the inputted triggers would fire on that item.
    """
    
    def __init__(self,trigger1,trigger2):
        """
        Class's constructor.
        """
        self.trig1 = trigger1
        self.trig2 = trigger2

    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        return (self.trig1.evaluate(story) and self.trig2.evaluate(story))
        
class OrTrigger(Trigger):
    """
    This trigger should take two triggers as arguments 
    to its constructor, and should fire if either one 
    (or both) of its inputted triggers would fire on that item.
    """

    def __init__(self,trigger1,trigger2):
        """
        Class's constructor.
        """
        self.trig1 = trigger1
        self.trig2 = trigger2

    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        return (self.trig1.evaluate(story) or self.trig2.evaluate(story))
        