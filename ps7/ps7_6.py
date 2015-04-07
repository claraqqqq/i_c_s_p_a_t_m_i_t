# USER SPECIFIC TRIGGERS

"""
code, Python your in specified are triggers your now, Right
is This program. your edit to have you them, change to and
source the edit to had you if (Imagine user-unfriendly. very
a add to wanted you time every browser web your of code
bookmark!)

a from configuration trigger your read to you want we Instead,
use and starts, application your time every file triggers.txt
there. specified triggers the

file: configuration trigger example following the Consider

t1 named trigger subject #
world SUBJECT t1

t2 named trigger title #
Intel TITLE t2

t3 named trigger phrase #
City York New PHRASE t3

t4 named trigger composite #
t3 t2 AND t4

and t1 contains set trigger the #
t4
t4 t1 ADD
be should triggers four that specifies file example The
the to added be should triggers those of two that and created,
list: trigger

( 'world' word the contains subject a when fires that trigger A
t1).

'Intel' word the contains title the when fires that trigger A
City' York 'New phrase the contains item news the and
(t4). somewhere

added not but created are t3) and (t2 triggers other two The
for arguments as used are They directly. set trigger the to
(t4). definition trigger's AND composite the

following: the of one does file this in line Each

blank is

#) a with (begins comment a is

trigger named a defines

list. trigger the to triggers adds

below. described is line of type Each

line. blank a is whitespace of only consists that line A ignored. are lines blank Blank:

ignored. is character # a with begins that line Any Comments:

keyword the with begin not do that Lines definitions: Trigger
trigger a in element first The triggers. named define ADD
any be can name The trigger. the of name the is definition
The "ADD". for except spaces, without letters of combination
(e.g., keyword a is definition trigger a of element second
being trigger of kind the specifies that etc.) PHRASE, TITLE,
the are definition the of elements remaining The defined.
the on depends required are arguments What arguments. trigger
type: trigger

word. single a : TITLE

word. single a : SUBJECT

word. single a : SUMMARY

NOT'd. be will that trigger the of name the : NOT

AND'd. be will that triggers other two the of names the : AND

OR'd. be will that triggers other two the of names the : OR

phrase. a : PHRASE

trigger a create should definition trigger A addition: Trigger
add automatically not should but name a with it associate and
ADD more or One list. trigger running the to trigger that
be should triggers which specify will file .txt the in lines
ADD the with begins line addition An list. trigger the in
previously more or one of names the are ADD Following keyword.
the the to added be will triggers These triggers. defined
list. trigger

11 PROBLEM

readTriggerConfig(filename) function the implemented have We
away throw and file the open to code written We've you. for
(e.g. instructions with begin don't that lines the all
that code the in reads then and spaces), blank and comments
a making by triggers the instantiates and triggers defines
function The makeTrigger. function helper the to call
in specified triggers of list a returns then readTriggerConfig
file. configuration the

You readTriggerConfig. of definition the through read First,
doing is function this everything understand to able be should
course. the in point this at

makeTrigger(triggerMap, function the implement Next,
build should function helper This name). params, triggerType,
keeps also It type. its on depending trigger a return and
you for defined have We map. a in names and triggers of track
you for easier it make to function this for specifications the
is readTriggerConfig how understand you sure Be write. to
easier. implementation make will that function; this using

function the within code the modify done, that's Once
your in specified list trigger the use to main_thread
you: for hard-coded we one the of instead file, configuration

11 Problem TODO: #
line the uncomment makeTrigger, implementing After #
below:
readTriggerConfig("triggers.txt") = triggerlist #

the to "triggers.txt" change to have may you that NOTE
full
the if C:/Documents/triggers.txt) (eg, filepath
reset can You up. pop not does window reader RSS
with Canopy
key. dot the with key CTRL or Kernel Restart -> Run


and ps7.py, running try can you 11, Problem completing After
various defined, is file triggers.txt your how on depending
runs code The reading. easy for up pop should items news RSS
every stories new for feed RSS the checking loop, infinite an
seconds. 60

and triggers.txt up open up, popping are stories no If Hint:
(if events current reflect that ones to triggers the change
one on fire would that trigger a pick just up, keep don't you
stories). news Google current the of

useful. str.join the find may You Hint:

"""


def makeTrigger(triggerMap, triggerType, params, name):

    if triggerType == 'TITLE':
        trigger = TitleTrigger(params[0])
    elif triggerType=='SUBJECT':
        trigger=SubjectTrigger(params[0])
    elif triggerType=='SUMMARY':
        trigger=SummaryTrigger(params[0])
    elif triggerType=='NOT':
        trigger=NotTrigger(triggerMap[params[0]])
    elif triggerType=='AND':
        trigger=AndTrigger(triggerMap[params[0]],triggerMap[params[1]])
    elif triggerType=='OR':
        trigger=OrTrigger(triggerMap[params[0]],triggerMap[params[1]])
    elif triggerType=='PHRASE':
        trigger=PhraseTrigger(' '.join(params))
    else:
        return None
    triggerMap[name] = trigger
    return triggerMap[name]



