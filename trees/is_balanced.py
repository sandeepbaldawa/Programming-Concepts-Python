# Class definition for a binary tree.
class Node:
  def __init__(self, data, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right


def height(node):
  return max(height(node.left), height(node.right)) + 1 if node else 0

def isBalanced(node):
  if not node:
     return True
  left_h = height(node.left)
  right_h = height(node.right)
  if abs(left_h - right_h) >1:
      return False
  else:
      return isBalanced(node.left) and isBalanced(node.right)

t = Node(24)
t.left = Node(18)
t.left.left = Node(10)
t.left.left.left = Node(7)
t.right = Node(36)
t.right.right = Node(54)
t.right.right.right = Node(80)
#height(t)
#height(Node(20))
#t.right.right = Node(1)
#t.right.right.right = Node(2)
#t.right.right.right.right = Node(3)
#print height(t)
print isBalanced(t)
