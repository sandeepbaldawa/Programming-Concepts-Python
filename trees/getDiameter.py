class Node:
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right

def getDiameter(node):
    if not node:
        return 0,0

    h_l, d_l = getDiameter(node.left)
    h_r, d_r = getDiameter(node.right)
    height = max(h_l, h_r) + 1
    diameter =  h_l + h_r + 1
    diameter=d_l if d_l > diameter else diameter
    diameter=d_r if d_r > diameter else diameter

    return height, diameter

myTree = Node(10)
myTree.left = Node(5)
myTree.right = Node(15)
myTree.left.left = Node(2)
myTree.left.right = Node(6)
myTree.right.left = Node(11)
myTree.right.right = Node(20)

print getDiameter(myTree)
