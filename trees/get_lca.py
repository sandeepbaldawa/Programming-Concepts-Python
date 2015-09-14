# https://www.youtube.com/watch?v=NBcqBddFbZw
# https://www.youtube.com/watch?v=bl-gwEwm8CM

from print_tree import *


def getLca(curr, A, B):
    assert(A != B)
    if not curr:
        return None

    # Try to find node A and node B
    if (curr == A or curr == B):
        return curr

    left = getLca(curr.left, A, B)
    right = getLca(curr.right, A, B)

    # if left and right are present, that parent is the lca
    if left and right:
        return curr

    return left if left else right

myTree = BinTree(1)
myTree.left = BinTree(2)
myTree.right = BinTree(3)
myTree.left.left = BinTree(4)
myTree.left.right = BinTree(5)
myTree.right.left = BinTree(6)
myTree.right.right = BinTree(7)
print(myTree)
tmp = getLca(myTree, myTree.left.right, myTree.left.left)
print " LCA of %s %s is %s" % (myTree.left.right.entry, myTree.left.left.entry, tmp.entry)
