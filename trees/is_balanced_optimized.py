# Class definition for a binary tree.


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def isBalanced_optimized(node):
    return height_optimized(node) != -2


def height_optimized(node):
    if not node:
        return -1

    left_h = height_optimized(node.left)
    if left_h == -2:
        return -2
    right_h = height_optimized(node.right)
    if right_h == -2:
        return -2
    if abs(left_h - right_h) > 1:
        return -2
    return max(isBalanced_optimized(node.left), isBalanced_optimized(node.right)) + 1


t = Node(24)
t.left = Node(18)
#t.left.left = Node(10)
#t.left.left.left = Node(7)
t.right = Node(36)
#t.right.right = Node(54)
#t.right.right.right = Node(80)
#height(t)
#height(Node(20))
#t.right.right = Node(1)
#t.right.right.right = Node(2)
#t.right.right.right.right = Node(3)
#print height(t)
print isBalanced_optimized(t)
