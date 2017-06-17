'''
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = 0
        if not root:
            return 0
            
        if root.left and not root.left.right and not root.left.left:
            res += root.left.val
        else:    
            res += self.sumOfLeftLeaves(root.left)
        
        res += self.sumOfLeftLeaves(root.right)    
        return res

    
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        summ = [0] # initialize result
     
        # Use the above recursive fucntion to evaluate sum
        self.leftLeavesSumRec(root, 0, summ)
        
        return summ[0]
    
    def leftLeavesSumRec(self, root, isLeft, summ):
        if root is None:
            return
     
        # Check whether this node is a leaf node and is left
        if root.left is None and root.right is None and isLeft == True:
            summ[0] += root.val
 
        # Pass 1 for left and 0 for right
        self.leftLeavesSumRec(root.left, 1, summ)
        self.leftLeavesSumRec(root.right, 0, summ)
