from print_tree import *

def get_all_paths(node, curr=""):
  if not node:
      return

  curr = curr + " " + str(node.entry)
  get_all_paths(node.left, curr)
  get_all_paths(node.right, curr)
  if not node.left and not node.right:
     print curr

t = BinTree(906, BinTree(2, BinTree(0), BinTree(4)), BinTree(10, BinTree(8), BinTree(12)))
print(t)

get_all_paths(t)
