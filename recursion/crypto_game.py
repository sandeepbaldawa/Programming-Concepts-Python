'''
 Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
 Input formula is a string; output is a digit-filled-in string or None.

Where are we spending more time?
if we run CProfile on CProfile.run('test()')
we see maximum time is spent inside valid function,
so how do we optimize the same?

In valid function we use eval which repeated parses
all tokens, we might not have to do this always.
copiling this once is fine

>>> f = lambda Y, M, E, U, O:(1*U+10*O+100*Y) == (1*E+10*M)**2
>>> f(2,1,7,9,8)
True
>>> f(1,2,3,4,5)
False

Check faster version in cryptogame_faster.py


'''

from __future__ import division
import itertools, string, re, time
import cProfile

def solve(formula):
    """Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
    Input formula is a string; output is a digit-filled-in string or None."""
    for f in fill_in(formula):
        if valid(f):
            return f


def fill_in(formula):
    "Generate all possible fillings-in of letters in formula with digits."
    letters = ''.join(set(re.findall('[A-Z]',formula))) #should be a string
    for digits in itertools.permutations('1234567890', len(letters)):
        table = string.maketrans(letters, ''.join(digits))
        yield formula.translate(table)

def valid(f):
    """Formula f is valid if and only if it has no
    numbers with leading zero, and evals true."""
    try:
        return not re.search(r'\b0[0-9]', f) and eval(f) is True
    except ArithmeticError:
        return False

tests = ("TWO + TWO == FOUR\n"
         "X/X == X\n"
         "A**N + B**N == C**N \n"
         "GLITTERS is not GOLD\n"
         "ONE < TWO and FOUR < FIVE\n"
         "ONE < TWO < THREE\n"
         "PLUTO not in set([PLANETS])\n"
         "ODD + ODD == EVEN\n"
         "sum(range(AA)) == BB\n"
         "sum(range(POP)) == BOBO\n"
         "RAMN == RA**3 + MN**3\n"
         "ATOM**0.5 == A + TO + M   \n").splitlines()

def test():
    t0 = time.clock()
    print tests

    for each in tests:
        t_each = time.clock()
        print "Problem : %s Result: %s" % (each, solve(each)),
        print " Time Taken : ", time.clock() - t_each
    print "Total Time Taken : ",  time.clock() - t0

print cProfile.run('test()')
