from print_tree import *
def getMax(n):
    if not n:
       return -1
    nleft = getMax(n.left)
    nright = getMax(n.right)
    return max(nleft, nright, n.entry)


t = BinTree(6, BinTree(2, BinTree(0), BinTree(4)), BinTree(10, BinTree(8), BinTree(12)))
print getMax(t)
