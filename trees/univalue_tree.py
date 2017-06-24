'''
Given a binary tree, count the number of uni-value subtrees.

A Uni-value subtree means all nodes of the subtree have the same value.

For example:
Given binary tree,
              5
             / \
            1   5
           / \   \
          5   5   5
return 4.

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.count = 0
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.helper(root)
        return self.count
    
    def helper(self, root):
        if not root:
            return True
        
        l_uni = self.helper(root.left)
        r_uni = self.helper(root.right)
        if l_uni and r_uni:
            if root.left and root.left.val != root.val: return False
            if root.right and root.right.val != root.val: return False
            self.count += 1
            return True
        return False  
