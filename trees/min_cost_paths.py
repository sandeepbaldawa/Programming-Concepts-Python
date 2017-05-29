'''
Sales Path

The car manufacturer Honda holds their distribution system in the form of a tree (not necessarily binary). 
The root is the company itself, and every node in the tree represents a car distributor that receives cars 
from the parent node and ships them to its children nodes. The leaf nodes are car dealerships that sell cars 
direct to consumers. In addition, every node holds an integer that is the cost of shipping a car to it.

Take for example the tree below:

alt

A path from Honda’s factory to a car dealership, which is a path from the root to a leaf in the tree, is called a Sales Path. The cost of a Sales Path is the sum of the costs for every node in the path. For example, in the tree above one Sales Path is 0→3→0→10, and its cost is 13 (0+3+0+10).

Honda wishes to find the minimal Sales Path cost in its distribution tree. Given a node rootNode, write an function getCheapestCost that calculates the minimal Sales Path cost in the tree.

Implement your function in the most efficient manner and analyze its time and space complexities.

For example:

Given the rootNode of the tree in diagram above

Your function would return:

7 since it’s the minimal Sales Path cost (there are actually two Sales Paths in the tree whose cost is 7: 0→6→1 and 0→3→2→1→1)

'''


minimum_cost = float['INF']
# sys.MAXINT
# Interview Kickstart
def getCheapestCost(rootNode, running_sum=0):
  '''that calculates the minimal Sales Path cost in the tree.
     args: rootNode
     return: Minimum Sales Path cost in the tree
     
     TEST CASES
     >>>getCheapestCost("")
        return 0
     >>>getCheapestCost() # lenth is "1"
        return rootNode.cost 
     >>>getCheapestCost() # costs same for 2 or more paths
     >>>getCheapestCost  100000-1
     >>>getCheapestCost 0
     
     DATA STRUCTURE
     TREE => Time => log(N)*k == O(N)
     Space => O(N)
     
     ALGORITHM =>
        - Initialize minimum_cost, running_cost = 0, 0
        - Traverse depthwise
        - Add cost of each node to running_cost
        - Reach the leaf minimum(minimum_cost, running_cost)
        - After traversing all leaves we return minimum_cost
        
     Psuedo Code
     
       def getCheapestCost(rootNode):
           minimum_cost = sys.maxint
           helper(rootNode, running_cost):
               if not rootNode: # Leaf nodes
                   return min(running_cost, minimum_cost)
               running_cost += rootNode.cost    
               m1 = helper(rootNode.left, running_cost) 
               m2 = helper(rootNode.right, running_cost) 
               return min(m1,m2)
     
     0→3→0→10
     0→3→2→1->1
       minimum_cost = sys.maxint
       def getCheapestCost(rootNode, running_sum=0): 
          if not rootNode:
             return min(running_sum, minimum_cost)
          for each in rootNode.children[]:
              running_sum += each.cost
              getCheapestCost(each, running_cost):
              
             
          
          def __init__(self, cost):
            self.cost = cost
            self.children = [] ************
            self.parent = None
          
  '''
  
  # leaf calculate min cost
  if not rootNode:
    return min(running_sum, minimum_cost) 
  for each in rootNode.children[]: 
      running_sum += each.cost  
      getCheapestCost(each, running_cost):
              

########################################## 
# Use the helper code below to implement #
# and test your function above           #
##########################################

# Sales Path => Path from root to leaf
# Cost => Sum of costs for each node

# A node 
class Node:

  # Constructor to create a new node
  def __init__(self, cost):
    self.cost = cost
    self.children = []
    self.parent = None
 
