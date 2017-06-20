'''
Pre-Order depth traversal
Method1:-
To make tree perfect make the leaf nodes NULL(or MAXINT)
when we store the same in a file else we can't reconstruct the tree

Method2:-
Store any two among pre-order, inorder or postorder
and reconstruct the tree
'''

import pickle
import sys
class Node():
    def __init__(self, val):
        self.left=self.right=None
        self.val = val

MAXINT = sys.maxint
def serialize(root, stream):
    '''Serialize the given Binary Tree with root '''
    if not root:
        stream.dump(MAXINT)
        return
    stream.dump(root.val)
    serialize(root.left)
    serialize(root.right)

def deserialize(stream):
    '''De-Serialize the given Binary Tree with given file stream '''
    try:
        data = pickle.load(stream)
        if data == MAXINT:
            return None
        
        root = Node(data)
        root.left = deserialize(stream)
        root.right = deserialize(stream)
        return root
    except pickle.UnpicklingError:
        return None
