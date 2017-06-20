'''
Given root of a binary tree, delete any subtrees whose nodes sum up to zero.
'''
def make_subtree_zero_rec(root):
    if not root:
        return
    left_sum = make_subtree_zero_rec(root.left)
    right_sum = make_subtree_zero_rec(root.right)
    
    if left_sum == 0:
        root.left = None
    elif right_sum == 0:
        root.right = None
    
    return root.val + left_sum + right_sum

def make_subtree_zero(root):
    sum = make_subtree_zero_rec(root)
    if sum == 0:
        root = None
    return root
