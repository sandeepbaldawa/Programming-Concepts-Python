# Class definition for a binary tree.


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def isSymmetric(node):
    return not node or helper(node.left, node.right)


def helper(left, right):
    if not left and not right:
        return True
    elif left and right:
        return left.data == right.data and helper(left.left, right.right) and helper(left.right, right.left)
    else: # not node.left or not node.right
        return False
     
    

t = Node(24)
t.left = Node(18)
t.left.left = Node(10)
t.left.left.left = Node(7)
t.right = Node(18)
t.right.right = Node(10)
t.right.right.right = Node(7)
#height(t)
#height(Node(20))
#t.right.right = Node(1)
#t.right.right.right = Node(2)
#t.right.right.right.right = Node(3)
#print height(t)
print isSymmetric(t)
