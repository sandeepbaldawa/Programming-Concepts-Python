def fib(N):
    '''Print first N fibonacci numbers'''
    print "First N:{0} fib numbers are ".format(N)
    a , b = 0 , 1
    for i in xrange(N):
        print a
        a , b = b, a+b

fib(5)
fib(2)
fib(1)
