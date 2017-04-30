#Pseudo code form a mirror of tree
'''
    4               4
  2    5   ==    5     2
1  3                3    1
'''
def mirror_tree(node):
    if not node return
    tmp = Node(node.val)
    tmp_right = mirror_tree(tmp_left)
    tmp_left = mirror_tree(tmp_right)
    return tmp
