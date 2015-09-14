# Class definition for a binary tree.
from print_tree import *

def isBalanced(node):
  return isBalancedHelper(node) != -2  

def isBalancedHelper(node):
  if not node:
     return True
  
  left_h = isBalancedHelper(node.left)
  if left_h == -2:
      return -2

  right_h = isBalancedHelper(node.right)
  if right_h == -2:
      return -2

  if abs(left_h - right_h) >1:
      return -2 
  else:
      return max(left_h, right_h) + 1


t = BinTree(906, BinTree(2, BinTree(0), BinTree(4)), BinTree(10, BinTree(8), BinTree(12)))
print(t)

print "Is balanced?", isBalanced(t)
