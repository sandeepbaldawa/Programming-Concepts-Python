import unittest
import random

class Node:
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right

def is_bst(node, low=-float('INF')-1, high=float('INF')):
	if not node:
		return True
	return (node.data > low and node.data < high) and is_bst(node.left, low, node.data) and is_bst(node.right, node.data, high)


class TruthTest(unittest.TestCase):
    def testBSTPositive(self):
    	myTree = Node(10)
    	myTree.left = Node(5)
    	myTree.right = Node(15)
        self.assertEqual(is_bst(myTree), True)

    def testBSTempty(self):
    	myTree = None
    	self.assertEqual(is_bst(myTree), True)    

    def testBSTPositive_Larger(self):
    	myTree = Node(10)
    	myTree.left = Node(5)
    	myTree.right = Node(15)
    	myTree.left.left = Node(2)
    	myTree.left.right = Node(6)
    	myTree.right.left = Node(11)
    	myTree.right.right = Node(20)
        
    	self.assertEqual(is_bst(myTree), True)    	

    def testBSTNegative_OneNode(self):
    	myTree = Node(10)
    	myTree.left = Node(10)
    	myTree.right = Node(15)
        self.assertEqual(is_bst(myTree), False)	

    def testBSTNegative_AllEqual(self):
    	myTree = Node(0)
    	myTree.left = Node(0)
    	myTree.right = Node(0)
        self.assertEqual(is_bst(myTree), False)	  

    def testBSTPositive_Onlyleft(self):
    	myTree = Node(10)
    	myTree.left = Node(0)
    	self.assertEqual(is_bst(myTree), True)	  


    def testBSTPositive_OnlyRight(self):
     	myTree = Node(10)
     	myTree.right = Node(15)
     	self.assertEqual(is_bst(myTree), True)	      

if __name__ == '__main__':
    unittest.main()
