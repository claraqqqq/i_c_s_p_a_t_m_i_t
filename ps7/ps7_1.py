# DATA STRUCTURE DESIGN 

"""
News. Google feed: RSS specific one about talk let's First,
is: feed News Google the for URL The

http://news.google.com/?output=rss

probably you'll browser, your in URL this load to try you If
by generated code XML the of interpretation browser's your see
browser's your with source XML the view can You feed. the
make not will probably it though function, Source" Page "View
the to connect you whenever Abstractly, you. to sense much
entry Each items. of list a receive you feed, RSS News Google
News Google a In item. news single a represents list this in
fields: following the has entry every feed,

story. news this for identifier unique globally A : guid

headline. story's news The : title

or Stories', 'Top (e.g. story this for tag subject A : subject
'Sports').

story. news the summarizing so or paragraph A : summary

story. entire the with web-site a to link A : link

Problem the Generalizing
because be, to it like we'd than trickier little a is This
differently bit little a structured is feeds RSS these of each
a with up come to is I Part in goal our So, others. the than
a store to use we'll that representation standard unified,
story. news

an want we done, and said is all When this? want we do Why
various from feeds RSS several aggregates that application
we way: same exact the in them of all on act can and sources
all feeds RSS various from stories news read to able be should
be reader, feed RSS an used ever you've If place. one in
going we're problem exact the solve to had has it that assured
pset! this in tackle to

1 PROBLEM

a into stream data a turning of process the is Parsing
We with. work to convenient more is that format structured
the parse and retrieve will that code with you provided have
feeds. news Yahoo and Google

that feeds the from information this of all Parsing
feat. small no is us gives Times/etc. York New Google/Yahoo/the
Pretend first: problem the of part easy an tackle let's So,
has and parsing, specific the done already has someone that
following the contain that variables with you left
story: news a for information

a as serves that string a - (GUID) identifier unique globally
entry this for name unique

string a - title

string a - subject

string a - summary

string a - content more to link

can we that object an in information this store to want We
in task, Your program. our of rest the in around pass then
a with starting NewsStory, class, a write to is problem, this
link) summary, subject, title, (guid, takes that constructor
also NewsStory appropriately. them stores and arguments as
methods: following the contain to needs

getGuid(self)
getTitle(self)
getSubject(self)
getSummary(self)
getLink(self)
an of element appropriate the return should method Each
and class the implemented have we if example, For instance.
call

long 'some 'mySubject', 'myTitle', NewsStory('foo', = test
'www.example.com') summary',
foo. return will test.getGuid() then
and short relatively be should problem this to solution The
do should methods get what review (please straightforward very
each). for code of lines multiple writing yourself find you if
test NewsStory the all NewsStory implemented have you Once
work. should cases

suite test a provided have we definition, class your test To
running and loading by code your test can You ps7_test.py. in
if tests NewsStory the for "OK" an see should You file. this
the run to code contains ps7.py Because correct. is code your
ps7 run to try not do you suggest we system, scraping RSS full
IDLE, in Instead, implementation. your test to directly .py
following: the do can you

* import ps7 from >>>
'some 'mySubject', 'myTitle', ps7.NewsStory('foo', = test >>>
'www.example.com') summary', long
definitions. class your on tests own your run then in load to
error, an getting are you If Instructions: Specific Canopy
instead: following the type
code your where directory the of path full the [insert cd >>>
resides]
* import ps7 from >>>
'some 'mySubject', 'myTitle', NewsStory('foo', = test >>>
'www.example.com') summary', long

"""

class NewsStory(object):
    
    def __init__(self, guid, title, subject, summary, link):
        self.guid = guid
        self.title = title
        self.subject = subject
        self.summary = summary
        self.link = link

    def getGuid(self):
        return self.guid

    def getTitle(self):
        return self.title

    def getSubject(self):
        return self.subject

    def getSummary(self):
        return self.summary

    def getLink(self):
        return self.link
        