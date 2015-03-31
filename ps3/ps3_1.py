# RADIATION EXPOSURE

"""
EXPOSURE RADIATION
loses atom unstable an which by process the is decay" "Radioactive
to refered commonly is what - particles ionizing emits and energy
very is and dangerous be can radiation to Exposure radiation. as
too to exposed not is one that ensure to measure to important
it. of much terribly

material the as time, over decreases material a of radioactivity The
x-axis The decay. this describes curve decay radioactive A decays.
activity of amount the measures y-axis the and time, measures
the as defined is 'Activity' sample. radioactive the by produced
transititions undergo sample the within nuclei the which at rate
any at emitted is radiation much how measures this simply, put -
the called is activity of measurement The time. in point one
curve: decay radioactive sample a is Here (Bq). Becquerel

images) full-sized view to pictures the on (Click

moved has Sarina say Let's solve. to like we'd problem the here's Now
of sample a is there her, to Unbeknownst apartment. new a into
that Initially apartment. the of walls the of one inside Cobalt-60
sample the after in moves she but activity, of MBq 10 had sample
years, 6 for apartment the in lives She years. 5 for there been has
to? exposed she was radiation much How leaves. then

curve decay radioactive the using out this figure actually can We
exposure radiation total her is know to want we What above. from
11. year to 5 year from

two the between area the to corresponds exposure radiation Total
radioactive blue the under and 11, = time and 5 = time at lines green
measures axis x the if - sense intuitive make should This curve. decay
curve the under area the then activity, measures axis y the and time,
total the approximately or, MBq*years, = activity) * (time measures
radioactive the in time her in to exposed was Sarina MBq of number
rays gamma of combination the is result this (technically, apartment
bit a gets this but to, exposed was she particles beta and
physicists!). Sorry, it. ignore we'll so complicated,

simple a Unlike this? calculate we do how But, good. so far, So
tell to way easy no have we - circle a or square, a say - shape
is. curve this under area the what

- here us help can that technique a learned have we However,
estimate to algorithm approximation an use Let's approximation.
the up splitting first by so do We'll curve! this under area the
them, of six case, this (in rectangles equally-sized into area
year): per rectangle one

rectangle each of area the out figure can we that, done we've Once
by found is rectangle a of area the that Recall easily. pretty
height The width. its by rectangle the of height the multiplying
rectangle: this of

by described is curve the If 5.0. at curve the of value the is
asking by curve the of value the obtain can we f, function, a
f(5.0). for

5.181 = f(5.0)
single this of area the So 1.0. is rectangle the of width The
radiation much how approximate To 5.181. = 1.0*5.181 is rectangle
successive each of area the calculate next we to, exposed was Sarina
total. the get to rectangle each of areas the up sum then and rectangle
of MBq 23 nearly to exposed was Sarina that find we this, do we When
3.154e6 * 23e6 by bombarded was apartment her (technically, radition
interested...). those for neutrons, 7.25e13 =

type the on exactly depends Sarina kill will this not or Whether
more discusses which link this (see to exposed was she radiation of
should she way, Either radiation). measuring of ways the about
refund. substantial a for landlord her ask probably

a radiation of amount the find to asked are you problem, this In
the completing by time of period some during to exposed is person
function: following

step): stop, radiationExposure(start, def
'''
exposed radiation of amount the returns and Computes
the Calls times. stop and start the between to
script) grading the in you for (defined f function
point. any at function the of value the obtain to

begins exposure which at time the integer, start:
ends exposure which at time the integer, stop:
that assume can You rectangle. each of width the float, step:
evenly. space the partition always will size step the

to exposed radiation of amount the float, returns:
times. stop and start between
'''
of value the what know to need you'll function this complete To
function a is There points. various at is curve decay radioactive the
your within from call can you that you for defined be will that if
problem. the for curve decay radioactive the describes that function

new a Open machine. own your on function this implement should You
your Complete "radiationExposure.py". it title and file Python Canopy
are you when and Canopy, in well code your Test file. this inside work
tutor this into definition your paste and cut correct, is it convinced
window.

own your on these test to sure Be With. Code Your Test to Cases Test
code your running before - output! same the get you that and - machine
webpage! this on

follows: as defined is f function curve the that Assume
f(x): def
math import
x) * 10*math.e**(math.log(0.5)/5.27 return

1: case Test
1) 5, radiationExposure(0, >>>
39.10318784326239
2: case Test
1) 11, radiationExposure(5, >>>
22.94241041057671
3: case Test
1) 11, radiationExposure(0, >>>
62.0455982538
4: case Test
1.5) 100, radiationExposure(40, >>>
0.434612356115

of 0.01 within be should answers Your cases: test these on note A
answer. correct the

Interest of Note Mathematical A
integration. called is curve a under area the finding of technique The
an is problem this in doing we're What calculus. from us to comes This
the using curve the under integral the finding of approximation
integral. Riemann a as known areas rectangular of summation
width the smaller the correct more and more becomes approximation This
becomes. rectangles the of
now you've before, calculus learned not you've If it. have you there So
covered! - integration - basics the of one got

"""

def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.
 
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to 
      between start and stop times.
    '''
    result = 0
    samples = (stop - start) / step
    for ii in range(int(samples)):
       result += f(start) * step
       start += step
    return result

# rewrite 1

def radiationExposure(start, stop, step):
    samples = int((stop-start) / step)
    res = 0
    for idx in range(samples):
       res += f(start+idx*step) * step  
    return res