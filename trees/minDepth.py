# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
   def minDepth(self, root):
        if not root: 
            return 0;
            
        l = self.minDepth(root.left);
        r = self.minDepth(root.right);
        
        return l + r + 1 if l == 0 or r == 0 else min(l, r) + 1;
         
