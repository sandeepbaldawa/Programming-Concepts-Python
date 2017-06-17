'''
You have a binary tree which consists of 0 or 1 in the way, that each node value is a LOGICAL AND between its children:


     0
   /   \
  0     1
 / \   / \
0   1  1  1
You need to write a code, which will invert given LEAF and put tree in a correct state.
'''

def generate(root):
  ''' Binary & of the children of a node is the current node's value''' 
  if not root:
    return 0
    
 if root.left and root.right:
    return generate(root.left) and generate(root.right)
 else:
    return root.val 
    
    
    
