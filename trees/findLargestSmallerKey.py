
res = 0
def findLargestSmallerKey(rootNode, num):
   if not rootNode:
      return None

   if num < rootNode.key:
      res = rootNode.key
      findLargestSmallerKey(rootNode.left, num)
   else:
      findLargestSmallerKey(rootNode.right, num)                                                 
