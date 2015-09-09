class Node():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def getMax(node, max=0):
    if not node:
        return max

    max = getMax(node.left, max)
    max = getMax(node.right, max)
    return max if max > node.data else node.data


myTree = Node(5)
myTree.left = Node(10)
myTree.right = Node(5)
myTree.left.left = Node(1000)
myTree.left.right = Node(3000)
myTree.right.left = Node(2000)
myTree.right.right = Node(4000)
print getMax(myTree)
