# Given target find value which is close to it in a bst
from print_tree import *

def getNearest(node, target, closest=None):
    if not node:
        return closest

    if node.entry == target:
        return node
    print node.entry
    if (closest is None or (abs(closest.entry - target) <  abs(node.entry - target))):
         closest = node
    if target < node.entry:
        closest = getNearest(node.left, target, closest)
    else:
        closest = getNearest(node.right, target, closest)
    return closest


t = BinTree(6, BinTree(2, BinTree(0), BinTree(4)), BinTree(10, BinTree(9), BinTree(12)))
print getNearest(t,9)
