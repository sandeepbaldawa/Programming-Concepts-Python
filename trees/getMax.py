from print_tree import *

def getMax(node, max=0):
    if not node:
        return max

    max = getMax(node.left, max)
    max = getMax(node.right, max)
    return max if max > node.entry else node.entry


t = BinTree(6, BinTree(2, BinTree(0), BinTree(4)), BinTree(10, BinTree(8), BinTree(12)))
print getMax(t)
