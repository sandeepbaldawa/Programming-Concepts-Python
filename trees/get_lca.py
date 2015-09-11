# https://www.youtube.com/watch?v=NBcqBddFbZw
# https://www.youtube.com/watch?v=bl-gwEwm8CM

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def getLca(curr, A, B): 
    assert(A != B) 
    if not curr:
        return None
    
    # Try to find node A and node B   
    if (curr == A or curr == B):
        return curr

    left = getLca(curr.left, A, B)
    right = getLca(curr.right, A, B)

    # if left and right are present, that parent is the lca 
    if left and right:
        return curr

    return left if left else right

myTree = Node(1)
myTree.left = Node(2)
myTree.right = Node(3)
myTree.left.left = Node(4)
myTree.left.right = Node(5)
myTree.right.left = Node(6)
myTree.right.right = Node(7)
tmp = getLca(myTree, myTree.left.right, myTree.left.left )   
print tmp.data
