# WORD TRIGGERS 

"""
generate will program your stories, news of set a Given
will alerts with Stories stories. those of subset a for alerts
be will stories other the and user, the to displayed be
as rules alerting represent will We discarded. silently
single a over evaluated is that rule a is trigger A triggers.
a example, For alert. an generate to fire may and story news
title whose story news every for fire could trigger simple
up set be may trigger Another "Microsoft". word the contained
the contained summary the where stories news all for fire to
up set be could trigger specific more a Finally, "Boston". word
words the both contained story news a when only fire to
summary. the in "Boston" and "Microsoft"

polymorphism. object use will we code, our simplify to order In
number a implement then and interface trigger a define will We
in interface trigger that implement that classes different of
ways. different

INTERFACE TRIGGER

following the implement should define you class trigger Each
implement must It transitively. or directly either interface,
object) (NewsStory item news a takes that method evaluate the
generated be should alert an if True returns and input an as
of implementation the use directly not will We item. that for
should exception an throws it why is which class, Trigger the
it use to attempt anyone

not will (you interface Trigger the implements below class The
an have will it from inherits that subclass Any this). modify
method evaluate the use will they default, By method. evaluate
own their define they unless superclass, the Trigger, in
some If instead. used be then would which function, evaluate
to calls method, evaluate() own its define to neglects subclass
cleanly) (albeit fails which Trigger.evaluate(), to go will it
exception: NotImplementedError the with

Trigger(object): class
story): evaluate(self, def
"""
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
"""
NotImplementedError raise
Trigger. from inherit that classes of number a define will We
other all which superclass, a is Trigger below, figure the In
Trigger to WordTrigger from arrow The from. inherit classes
is WordTrigger a - Trigger from inherits WordTrigger that means
WordTrigger. from inherit classes other that Note . Trigger a



view] full-size a for image above the on [Click

TRIGGERS WORD WHOLE

let's interesting; isn't fires always that trigger a Having
news about alerted be to want may user A are. that some write
simple a instance, For words. specific contain that items
the contains title whose item news every for fire could trigger
a create will you problems, following the In "Microsoft". word
that classes three implement and class abstract WordTrigger
class. this from inherit

For present. is word whole the when fire should trigger The
on: fire should "soft" for trigger a example,

cuddly. and soft are bears Koala

soft. are that pillows prefer I

great. are drinks Soft

pink! new the Soft's

football. the threw he as exclaimed he "Soft!"

on: fire not should But

Preview. Consumer 8 Windows the released recently Microsoft

be! can they softest the clothes my makes Downey

apostrophe the with case the especially tricky, little a is This
any or space a that pretend parsing, your of purpose the For .
you've If separator. word a is string.punctuation in character
interpreter your to go before, string.punctuation seen never
type: and
string import >>>
string.punctuation print >>>
is. it what with comfortable get to bit a this with around Play
certainly almost will strings of methods replace and split The
part. this tackle you as helpful be
useful upper and/or lower methods string the find also may You
problem. this for

2 PROBLEM

should It WordTrigger. class, abstract trigger word a Implement
constructor. class's the to argument an as word string a in take

new one has It Trigger. of subclass a be should WordTrigger
It text. argument string one in takes which isWordIn, method,
False text, in present is word word whole the if True returns
method This examples. above the in described as otherwise,
method. this Implement case-sensitive. be not should

Hint
procedure a write to want may you punctuation, with deal To
space. a with string a in mark punctuation every replaces that
a into result the up break to methods string use then can You
words. distinct of list

directly be not will we class, abstract an is this Because
its inherit should WordTrigger WordTriggers. any instantiating
can we now because this do We Trigger. from method evaluate
method. isWordIn its use that WordTrigger of subclasses create
now except interface, Trigger the like much is it way, this In
its in used is class WordTrigger this from code actual
subclasses.

3 PROBLEM

subclasses: three WordTrigger's implement to ready now are You
SummaryTrigger. and SubjectTrigger, TitleTrigger,

a when fires that TitleTrigger, class, trigger word a Implement
an be should word The word. given a contains title item's news
be not should trigger This constructor. class's the to argument
being as "intel" and "Intel" treat should (it case-sensitive
equal).

used be could trigger of type this of instance an example, For
the in occurred "Intel" word the whenever alert an generate to
alert an generate could instance Another item. news a of title
item. an of title the in occurred "Microsoft" word the whenever

in defined be should methods what about carefully Think
the from inherited be should methods what and TitleTrigger
lines 3 as few as in implemented be can class This superclass.
code!

Hint
classes SummaryTrigger and SubjectTrigger, TitleTrigger, Your
section the Re-read method! ONE only define each should
you've if page, this of top the at INTERFACE', 'TRIGGER
here. to up we're what forgotten
and SubjectTrigger, TitleTrigger, that remember Further,
that means This WordTrigger. of subclasses are SummaryTrigger
it if as WordTrigger within defined method any use can they
themselves. within definied were
might that WordTrigger within define you did method What Hint:
in method one the implementing in useful incredibly super be
SummaryTrigger and SubjectTrigger, TitleTrigger, the of each
classes?

unit TitleTrigger the TitleTrigger, implemented you've Once
check. to ps7_test.py Run pass. should suite test our in tests

inps7. code modify you time instructions:Every specific Canopy
to pygo

your on dot the with CTRL the hit (or Kernel Restart -> Run
keyboard)
you time every this do to have You ps7_test.py. running before
fileps7_test.py, the run to want fileps7.pyand the modify
the in incorporated be not will former the to changes otherwise
latter.

4 PROBLEM

when fires that SubjectTrigger, class, trigger word a Implement
be should word The word. given a contains subject item's news a
not should trigger This constructor. class's the to argument an
case-sensitive. be

unit SubjectTrigger the SubjectTrigger, implemented you've Once
pass. should suite test our in tests

5 PROBLEM

when fires that SummaryTrigger, class, trigger word a Implement
be should word The word. given a contains summary item's news a
not should trigger This constructor. class's the to argument an
case-sensitive. be

unit SummaryTrigger the SummaryTrigger, implemented you've Once
pass. should suite test our in tests

TitleTrigger, WordTrigger, for code your Enter #
box this in SummaryTrigger and SubjectTrigger, #

"""

import string

class WordTrigger(Trigger):
    def __init__(self, word):
        self.word = word
    def isWordIn(self, text):   
        text = text.lower()
        word = self.word.lower()
        for punct in string.punctuation:
            text = text.replace(punct,' ')
        text_list = text.split()
        return word in text_list 

class TitleTrigger(WordTrigger):
    def __init__(self, word):
        WordTrigger.__init__(self, word)
    def evaluate(self, story):
        return self.isWordIn(story.getTitle())

class SubjectTrigger(WordTrigger):
    def __init__(self, word):
        WordTrigger.__init__(self, word)
    def evaluate(self, story):
        return self.isWordIn(story.getSubject())

class SummaryTrigger(WordTrigger):
    def __init__(self, word):
        WordTrigger.__init__(self, word)
    def evaluate(self, story):
        return self.isWordIn(story.getSummary())
        