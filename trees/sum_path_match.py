def sum_path_match(tree, target):
    if not tree:
        return False
        
    if not tree.left and tree.right:    
        return abs(target - tree.node) == 0

    if abs(target - tree.node) == 0:
        return True
    return sum_path_match(tree.left, target - tree.node) or sum_path_match(tree.right, target - tree.node):
    return False
