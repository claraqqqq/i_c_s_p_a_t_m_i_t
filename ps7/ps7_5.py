# FILTERING

"""
and fetch will it and ps7.py, run can you point, this At
pop-up little in you for items news Yahoo and Google display
them. of All items? news many How windows.

the of all gets ps7.py in you given we've code the now, Right
nice, is This result. the displays and minute, every feeds
the the only out filter to was here goal the remember, but,
wanted. we stories

10 PROBLEM

that triggerlist) filterStories(stories, function, a Write
and triggers, of list a and stories news of list a in takes
the of any which for stories the only of list a returns
that - unique be should stories of list The on. fires triggers
if example, For list. the in duplicates any include not do is,
one list the in StoryA include only StoryA, on fire triggers 2
time.

the All ps7_test.py. file the run 10, Problem completing After
pass. now should tests

inps7. code modify you time instructions:Every specific Canopy
to pygo
your on dot the with CTRL the hit (or Kernel Restart -> Run
keyboard)
you time every this do to have You ps7_test.py. running before
fileps7_test.py, the run to want fileps7.pyand the modify
in incorporated be not will former the to changes otherwise
latter. the

ps7.py, running try can you 10, Problem completing after Also
hard some by filtered up, pop should items news RSS various and
bottom. the near code some in you for defined triggers -coded
new for feed RSS the checking loop, infinite an runs code The
the of bottom the at "Exit" Press seconds. 60 every stories
program. the of out exit to window popup

please filterStories, function the to addition In Note:
TitleTrigger, WordTrigger, of definitions your provide
the in PhraseTrigger and SummaryTrigger, SubjectTrigger,
box. following

"""

# Enter your code for WordTrigger, TitleTrigger,
# SubjectTrigger, SummaryTrigger, PhraseTrigger, and 
# filterStories in this box

# Enter your code for WordTrigger, TitleTrigger,
# SubjectTrigger, SummaryTrigger, PhraseTrigger, and 
# filterStories in this box

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
               
def filterStories(stories, triggerlist):
    if len(stories) == 0:
        return False
    story_list = []
    for story in stories:
        for trigger in triggerlist:
            if trigger.evaluate(story):
                story_list.append(story)
                break
    return story_list
    
    