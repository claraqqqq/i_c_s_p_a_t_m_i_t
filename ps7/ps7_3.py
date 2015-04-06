# COMPOSITE TRIGGERS

"""
TRIGGERS COMPOSITE

interesting, mildly are page previous the from triggers the So
earlier the 'compose' to want we better: do to want we but
we instance, For rules. alert powerful more up set to triggers,
"stock" and "google" both when only alert an raise to want may
now right express can't we idea (an item news the in present were
).

be not should and triggers word not are triggers these that Note
WordTrigger. of subclasses

6 PROBLEM

(NotTrigger). trigger NOT a Implement

output the inverting by output its produce should trigger This
other this take should trigger NOT The trigger. another of
constructor? its (Why constructor. its to argument an as trigger
in... takes evaluate parameters what change can't we Because
news a and T trigger a given So, polymorphism). our break that'd
should method evaluate trigger's NOT the of output the x, item
T.evaluate(x). not to equivalent be

pass. should tests unit NotTrigger the done, is this When

inps7. code modify you time instructions:Every specific Canopy
to pygo
your on dot the with CTRL the hit (or Kernel Restart -> Run
keyboard)
you time every this do to have You ps7_test.py. running before
fileps7_test.py, the run to want fileps7.pyand the modify
the in incorporated be not will former the to changes otherwise
latter.

7 PROBLEM

(AndTrigger). trigger AND an Implement

its to arguments as triggers two take should trigger This
the of both if only story news a on fire should and constructor,
item. that on fire would triggers inputted

pass. should tests unit AndTrigger the done, is this When

8 PROBLEM

(OrTrigger). trigger OR an Implement

its to arguments as triggers two take should trigger This
its of both) (or one either if fire should and constructor,
item. that on fire would triggers inputted

pass. should tests unit OrTrigger the done, is this When

( problem this in classes three the to addition In Note:
your provide please OrTrigger), and AndTrigger, NotTrigger,
box. following the in TitleTrigger and WordTrigger of definitions

"""

# TODO: WordTrigger
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
        
        
class NotTrigger(Trigger):
    def __init__(self, other_trigger):
        self.other_trigger = other_trigger
    def evaluate(self, story):
        return not self.other_trigger.evaluate(story)        

class AndTrigger(Trigger):
    def __init__(self,  trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2
    def evaluate(self, story):
        return self.trigger1.evaluate(story) and self.trigger2.evaluate(story)

class OrTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2
    def evaluate(self, story):
        return self.trigger1.evaluate(story) or self.trigger2.evaluate(story)
