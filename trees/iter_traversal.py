from print_tree import *
import random
import itertools

def random_gen(low, high):
    while True:
        yield random.randrange(low, high)

gen = list(random_gen(1, 100))
print gen       
t = BinTree(6, BinTree(2, BinTree(0), BinTree(4)), BinTree(10, BinTree(8), BinTree(12)))
print(t)