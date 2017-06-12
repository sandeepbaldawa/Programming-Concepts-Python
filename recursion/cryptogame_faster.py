# --------------
# User Instructions
#
# Modify the function compile_formula so that the function
# it returns, f, does not allow numbers where the first digit
# is zero. So if the formula contained YOU, f would return
# False anytime that Y was 0

from __future__ import division
import itertools, string, re, time
import cProfile


def compile_formula(formula, verbose=False):
    """Compile formula into a function. Also return letters found, as a str,
    in same order as parms of function. The first digit of a multi-digit
    number can't be 0. So if YOU is a word in the formula, and the function
    is called with Y eqal to 0, the function should return False."""

    # modify the code in this function.

    letters = ''.join(set(re.findall('[A-Z]', formula)))
    parms = ', '.join(letters)
    words = re.split('([A-Z]+)', formula)
    length_words = [w for w in words if len(w) > 1 and all([c in string.uppercase for c in w])]
    first_chars = list(set([w[0] for w in length_words]))
    conditions = " and ".join(["%s != 0" % c for c in first_chars])

    tokens = map(compile_word, words)
    body = ''.join(tokens) if not conditions else ''.join(tokens) + " and " + conditions
    f = 'lambda %s: %s' % (parms, body)
    if verbose: print f
    return eval(f), letters


def compile_word(word):
    """Compile a word of uppercase letters as numeric digits.
    E.g., compile_word('YOU') => '(1*U+10*O+100*Y)'
    Non-uppercase words uncahanged: compile_word('+') => '+'"""
    if word.isupper():
        terms = [('%s*%s' % (10 ** i, d))
                 for (i, d) in enumerate(word[::-1])]
        return '(' + '+'.join(terms) + ')'
    else:
        return word


def faster_solve(formula):
    """Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
    Input formula is a string; output is a digit-filled-in string or None.
    This version precompiles the formula; only one eval per formula."""
    f, letters = compile_formula(formula)
    for digits in itertools.permutations((1, 2, 3, 4, 5, 6, 7, 8, 9, 0), len(letters)):
        try:
            if f(*digits) is True:
                table = string.maketrans(letters, ''.join(map(str, digits)))
                return formula.translate(table)
        except ArithmeticError:
            pass


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
        print "Problem : %s Result: %s" % (each, faster_solve(each)),
        print " Time Taken : ", time.clock() - t_each
    print "Total Time Taken : ",  time.clock() - t0

#print cProfile.run('test()')
