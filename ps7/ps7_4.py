# PHRASE TRIGGERS

"""
TRIGGERS PHRASE

that trigger a writing of way no have you point, this At
how know you triggers only the -- City" York "New on matches
AND "New" on fire would that trigger a be would write to
"New phrase the on fires also which -- "City" AND "York"
fix to time It's city". the love University York at students
will we match, exact an for asking you're here Since this.
more little a be we'll but match, cases the that require
match: will City" York "New So, matching. word on flexible

premiere movie sees City York New

cafe famous City's York New of heart the In

Cityrandomtexttoproveapointhere York New

match: not will but

city york new love I

City!!!!!!!!!!!!!! York New love I

9 PROBLEM

a when fires that (PhraseTrigger) trigger phrase a Implement
or title, subject, story's the of any in is phrase given
class's the to argument an be should phrase The summary.
as helpful, in operator Python the find may You constructor.
in:

City's York New of heart the "In in City" York "New print >>>
cafe" famous
True
city" york new love "I in City" York "New print >>>
False
pass. should tests unit PhraseTrigger the done, is this When

inps7. code modify you time instructions:Every specific Canopy
to pygo
your on dot the with CTRL the hit (or Kernel Restart -> Run
keyboard)
you time every this do to have You ps7_test.py. running before
fileps7_test.py, the run to want fileps7.pyand the modify
in incorporated be not will former the to changes otherwise
latter. the

(PhraseTrigger) problem this in class the to addition In Note:
WordTrigger, of definitions your provide please ,
box. following the in SummaryTrigger and SubjectTrigger, TitleTrigger,

"""

# Enter your code for WordTrigger, TitleTrigger,
# SubjectTrigger, SummaryTrigger, and PhraseTrigger in this box

c# Enter your code for WordTrigger, TitleTrigger,
# SubjectTrigger, SummaryTrigger, and PhraseTrigger in this box

class WordTrigger(Trigger):
    def __init__(self, word):
        self.word = word   
    def isWordIn(self, text):
        text = text.lower()        
        word = self.word.lower()
        for punc in string.punctuation:
            text = text.replace(punc, ' ')
        text_list = text.split()
        return word in text_list   
        

# TODO: TitleTrigger
class TitleTrigger(WordTrigger):   
    def __init__(self, word):
        WordTrigger.__init__(self, word) 
    def evaluate(self, story):
        return self.isWordIn(story.getTitle())
    
            
# TODO: SubjectTrigger
class SubjectTrigger(WordTrigger):
    def __init__(self, word):
        WordTrigger.__init__(self, word)  
    def evaluate(self, story):
        return self.isWordIn(story.getSubject())
        
        
# TODO: SummaryTrigger
class SummaryTrigger(WordTrigger):
    def __init__(self, word):
        WordTrigger.__init__(self, word)   
    def evaluate(self, story):
        return self.isWordIn(story.getSummary())

class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase
    def evaluate(self, story):
        return self.phrase in story.getTitle() or \
               self.phrase in story.getSummary() or \
               self.phrase in story.getSubject()
               