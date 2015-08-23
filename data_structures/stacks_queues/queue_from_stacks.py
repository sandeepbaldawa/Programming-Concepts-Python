"""
1. Stack
2. Queue
3. Queue From Stacks
"""

class Node:  
     def __init__(self, data=None):  
       self.next = None  
       self.data = data 
         
  
class Stack:
	def __init__(self):  
		self.head = None

	def push(self, data):
		if not self.head:
			self.head = Node(data)
			self.head.next = None
		else:
			tmp = Node(data)
			tmp.next = self.head
			self.head = tmp	

	def pop(self):
		if not self.head:
			print "Cannot pop from empty stack"
			return None
		else:
			tmp = self.head
			self.head = tmp.next
			tmp.next = None
		return tmp.data

	def peek(self):
		if not self.head:
			return None
		else:
			return self.head.data

class Queue:
	def __init__(self):  
		self.head = None
		self.tail = None

	def enqueue(self, data):
		tmp = Node(data)
		tmp.next = None
		
		if self.tail:
			self.tail.next = tmp
		
		self.tail = tmp

		if not self.head:
			self.head = self.tail
	
	def dequeue(self):
		if not self.head:
			return head
        
        if not self.head.next:
        	tail = None

		tmp = self.head
		self.head = self.head.next

		return tmp.data

class QueueWithStacks:
	def __init__(self):  
		self.stack1 = Stack()
		self.stack2 = Stack()

	def enqueue(self, data):
		self.stack1.push(data)
        
	def dequeue(self):
		if self.stack2.peek():
			return self.stack2.pop()
		elif self.stack1.peek():
			while(self.stack1.peek()):
				self.stack2.push(self.stack1.pop())
			return self.stack2.pop()
		else:
			return None	

mystack = Stack()
mystack.push(10)
mystack.push(20)
mystack.push(30)
print mystack.pop()
print mystack.pop()
print mystack.pop()
print mystack.pop()
print mystack.peek()

myqueue = Queue()
myqueue.enqueue(10)
print myqueue.dequeue()
myqueue.enqueue(20)
print myqueue.dequeue()

myqueue = QueueWithStacks()
myqueue.enqueue(10)
print myqueue.dequeue()
myqueue.enqueue(20)
print myqueue.dequeue()
