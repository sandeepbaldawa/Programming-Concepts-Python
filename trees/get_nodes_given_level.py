from print_tree import *
import Queue


class Solution:

    def __init__(self):
        self.q1 = Queue.Queue()
        self.currLevel = self.currCount = 0
        self.prevCount = 1
        self.results = []

    def getNodesForLevel(self, node, K):
        self.q1.put(node)
        while not self.q1.empty():
            print "Current level is %s" % self.currLevel
            out = ""

            while self.prevCount > 0:
                curr = self.q1.get()
                if self.currLevel == K:
                    self.results.append(curr)
                self.prevCount -= 1
                out += str(curr.entry) + " "

                if curr.left:
                    self.q1.put(curr.left)
                    self.currCount += 1

                if curr.right:
                    self.q1.put(curr.right)
                    self.currCount += 1
            print out
            if self.currLevel == K:
                self.printResults()
                return
            self.currLevel += 1
            self.prevCount = self.currCount
            self.currCount = 0

    def printResults(self):
        out = ""
        print " Nodes at Level %s are" % self.currLevel
        for each in self.results:
            out += str(each.entry) + " "
        print out

myTree = BinTree(3)
myTree.left = BinTree(2)
myTree.right = BinTree(5)
myTree.left.left = BinTree(1)
myTree.left.right = BinTree(0)
myTree.left.right.left = BinTree(-1)
myTree.left.right.right = BinTree(-2)
myTree.right.left = BinTree(4)
myTree.right.right = BinTree(6)
print(myTree)
mySolution = Solution()
mySolution.getNodesForLevel(myTree, 3)





"""

mySolution.getNodesForLevel(myTree, 0)
   --3---  
  /      \ 
 -2-     5 
/   \   / \
1   0-  4 6
   /  \    
  -1 -2    
Current level is 0
3 
 Nodes at Level 0 are
3 


mySolution.getNodesForLevel(myTree, 1)
  --3---  
  /      \ 
 -2-     5 
/   \   / \
1   0-  4 6
   /  \    
  -1 -2    
Current level is 0
3 
Current level is 1
2 5 
 Nodes at Level 1 are
2 5 



mySolution.getNodesForLevel(myTree, 2)
   --3---  
  /      \ 
 -2-     5 
/   \   / \
1   0-  4 6
   /  \    
  -1 -2    
Current level is 0
3 
Current level is 1
2 5 
Current level is 2
1 0 4 6 
 Nodes at Level 2 are
1 0 4 6 


mySolution.getNodesForLevel(myTree, 3)
   --3---  
  /      \ 
 -2-     5 
/   \   / \
1   0-  4 6
   /  \    
  -1 -2    
Current level is 0
3 
Current level is 1
2 5 
Current level is 2
1 0 4 6 
Current level is 3
-1 -2 
 Nodes at Level 3 are
-1 -2 

"""
