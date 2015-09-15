from print_tree import *
def getDiameter(node):
    if not node:
        return 0, 0

    h_l, d_l = getDiameter(node.left)
    h_r, d_r = getDiameter(node.right)
    height = max(h_l, h_r) + 1
    diameter = h_l + h_r + 1
    diameter = d_l if d_l > diameter else diameter
    diameter = d_r if d_r > diameter else diameter

    return height, diameter

myTree = BinTree(1)
myTree.left = BinTree(5)
myTree.right = BinTree(15)
myTree.left.left = BinTree(2)
myTree.left.right = BinTree(6)
myTree.right.left = BinTree(11)
myTree.right.right = BinTree(20)
print(myTree)

print getDiameter(myTree)
