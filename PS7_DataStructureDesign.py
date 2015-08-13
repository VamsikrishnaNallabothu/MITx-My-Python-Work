#PS7_DataStructureDesign
#NVK
# Enter your code for NewsStory in this box
class NewsStory(object):
    """
    Represents a concrete news through its guid, title, 
    subject, summary and link.
    
    GUID - a string that serves as a unique name for this news.
    Title - news title.
    Subject - news subject.
    Summary - news summary.
    Link - link to more content.
    """
    
    def __init__(self,guid, title, subject, summary, link):
        """
        Initialize the news content.
        """
        self.guid = guid 
        self.title = title
        self.subject = subject
        self.summary = summary
        self.link = link
    
    def getGuid(self):
        """
        Gets news GUID.
        """
        return self.guid
        
    def getTitle(self):
        """
        Gets news title.
        """
        return self.title
        
    def getSubject(self):
        """
        Gets news subject.
        """
        return self.subject
        
    def getSummary(self):
        """
        Gets news summary.
        """
        return self.summary
                
    def getLink(self):
        """
        Gets news link.
        """
        return self.link
        
