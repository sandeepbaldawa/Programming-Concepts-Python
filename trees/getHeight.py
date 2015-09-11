class Node:
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right

def getHeight(node):
	if not node:
		return 0

	l_h = getHeight(node.left)
	r_h = getHeight(node.right)
	return max(r_h, l_h) + 1

myTree = Node(5)
myTree.left = Node(10)
myTree.right = Node(5)
myTree.left.left = Node(1000)
myTree.left.right = Node(3000)
myTree.right.left = Node(2000)
myTree.right.right = Node(4000)
myTree.right.right.left = Node(4000)
myTree.right.right.right = Node(4000)
myTree.right.right.right.left = Node(4000)
myTree.right.right.right.right = Node(4000)
print getHeight(myTree)
