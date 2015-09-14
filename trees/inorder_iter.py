import Queue
class Node:
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right

def print_postorder_iterative(node):
	stack = Queue.LifoQueue()
	stack.put(node)
	prev = None
	while not stack.empty(): 
		curr = stack.get()
		stack.put(curr)
		if (prev == None or prev.left == curr or prev.right == curr):
			if curr.left != None:
				stack.put(curr.left)
			elif curr.right != None:
				stack.put(curr.right)
			else:
				stack.get()
				print curr.data	
		elif curr.left == prev:
			if curr.right:
				stack.put(curr.right)
			else:
				stack.get()
				print curr.data	
		elif curr.right == prev:
			stack.get()
			print curr.data

		prev = curr		


def print_inorder_iterative(node):
	stack = Queue.LifoQueue()
	stack.put(node)
	prev = None
	while not stack.empty(): 
		curr = stack.get()
		stack.put(curr)
		if (prev == None or prev.left == curr or prev.right == curr):
			if curr.left != None:
				stack.put(curr.left)
			elif curr.right != None:
				print curr.node
				stack.put(curr.right)
			else:
				stack.get()
				print curr.data	
		elif curr.left == prev:
			print curr.data
			if curr.right:
				stack.put(curr.right)
			else:
				stack.get()
		elif curr.right == prev:
			stack.get()
			#print curr.data

		prev = curr		




"""	
myTree = Node(1)
myTree.left = Node(2)
myTree.right = Node(3)
myTree.left.left = Node(4)
myTree.left.right = Node(5)
myTree.right.left = Node(6)
myTree.right.right = Node(7)
"""

myTree = Node(10)
myTree.left = Node(9)
myTree.right = Node(6)
myTree.left.left = Node(4)
myTree.left.right = Node(5)
myTree.right.left = Node(6)
myTree.right.right = Node(7)


print print_inorder_iterative(myTree)