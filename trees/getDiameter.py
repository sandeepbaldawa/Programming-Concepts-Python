# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        h, d = self.helper(root)
        return d
    
    def helper(self, root):
        if not root:
            return (0, 0)
        
        h_l, d_l = self.helper(root.left)
        h_r, d_r = self.helper(root.right)
        
        h = 1 + max(h_l, h_r)
        d = max((h_l + h_r), d_l, d_r)
        return (h, d)
