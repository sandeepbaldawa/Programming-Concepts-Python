# This uses one queue and two counter variables

import Queue
class Node:
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right

def print_level_wise(node):
	q = Queue.Queue()
	q.put(node)
	levelCount = 1  # Each time you dequeue current element decrease this
	currCount = 0   # Count of children in the queue for current node(s)
	curr = 1

	output = ""
	while(levelCount > 0):
		curr = q.get()
		
		levelCount -= 1   # Each time you dequeue current element decrease this
		output += str(curr.data) + " "	
		
		if curr.left:
			q.put(curr.left)
			currCount += 1 # Each time you enqueue current element children increment this

		if curr.right:
			q.put(curr.right)
			currCount += 1 # Each time you enqueue current element children increment this
		
		if levelCount == 0:
			levelCount = currCount
			currCount = 0
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
