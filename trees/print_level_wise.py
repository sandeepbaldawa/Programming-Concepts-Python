# Using two queues
# This can be improved by using one queue and few variables
import Queue
class Node:
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right

def print_level_wise(node):
	q1 = Queue.Queue()
	q2 = Queue.Queue()
	q1.put(node)
	output = ""
	while(not q1.empty() or not q2.empty()):
		if not q1.empty():
			while not q1.empty():
				curr = q1.get()
				if curr == None:
					break
				q2.put(curr.left)
				q2.put(curr.right)
				output += str(curr.data) + " "	
		else:
			while not q2.empty():
				curr = q2.get()
				if curr == None:
					break
				q1.put(curr.left)
				q1.put(curr.right)
				output += str(curr.data) + " "
		print output
		output = ""		

myTree = Node(10)
myTree.left = Node(5)
myTree.right = Node(15)
myTree.left.left = Node(2)
myTree.left.right = Node(6)
myTree.right.left = Node(11)
myTree.right.right = Node(20)

print print_level_wise(myTree)
