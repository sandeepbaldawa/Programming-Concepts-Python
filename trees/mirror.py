#Pseudo code form a mirror of tree
'''
    4               4
  2    5   ==    5     2
1  3                3    1
'''
def mirror(n):
    if !n:
       return
     nleft = traverse(n.left)
     nright = traverse(n.right)
     n.left = nright
     n.right = nleft
     return n
