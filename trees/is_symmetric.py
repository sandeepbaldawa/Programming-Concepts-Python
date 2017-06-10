# Class definition for a binary tree.


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def isSymmetric(self, A):
        return self.isMirror(A, A)
        
    def isMirror(self, root1, root2):
        if not root1 and not root2:
            return True
        
        if root1 and root2:
            l_s = self.isMirror(root1.left, root2.right) 
            r_s = self.isMirror(root1.right, root2.left)
            return l_s and r_s and root1.val == root2.val
        
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
