from print_tree import *


def PrintLeftBoundary(node, isBoundary=True):
    if not node:
        return
    if (not node.left and not node.right) or isBoundary:
        print node.entry
    PrintLeftBoundary(node.left, isBoundary)
    PrintLeftBoundary(node.right, isBoundary and not node.left)


def PrintRightBoundary(node, isBoundary=True):
    if not node:
        return

    PrintLeftBoundary(node.left, isBoundary and not node.right)
    PrintLeftBoundary(node.right, isBoundary)
    if (not node.left and not node.right) or isBoundary:
        print node.entry


def printBoundary(node):
    if node:
        print node.entry
        PrintLeftBoundary(node.left)
        PrintRightBoundary(node.right)

myTree = BinTree(3)
myTree.left = BinTree(2)
myTree.right = BinTree(5)
myTree.left.left = BinTree(1)
myTree.left.right = BinTree(0)
myTree.left.right.left = BinTree(-1)
myTree.left.right.right = BinTree(-2)
myTree.right.left = BinTree(4)
myTree.right.right = BinTree(6)
print(myTree)
printBoundary(myTree)
