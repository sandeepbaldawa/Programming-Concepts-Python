class BinTree:
    """
    >>> t = BinTree(6, BinTree(2, BinTree(0), BinTree(4)), BinTree(10, BinTree(8), BinTree(12)))
    >>> t
    BinTree(6, BinTree(2, BinTree(0), BinTree(4)), BinTree(10, BinTree(8), BinTree(12)))
    >>> print(t)
      -6-  
     /   \ 
     2   10
    / \ /  \
    0 4 8 12
    """
    def __init__(self, entry, left=None, right=None):
        self.entry = entry
        self.left = left
        self.right = right
 
    def __repr__(self): # used by the interpreter
        args = repr(self.entry)
        if self.left or self.right:
            args += ', {0}, {1}'.format(repr(self.left), repr(self.right))
        return 'BinTree({0})'.format(args)
 
    def __str__(self): # used by print() and str()
        return tree_string(self)
 
# Tree printing functions, kindly provided by Joseph Hui. #
 
def tree_string(tree):
    return "\n".join(tree_block(tree)[0])
 
def tree_block(tree):
    """Returns a list of strings, each string being
    one line in a rectangle of text representing the
    tree.
    Also returns the index in the string which is
    centered above the tree's root.
 
    num_width: The width of the widest number in the tree (100 => 3)
    """
    #If no children, just return string
    if tree.left is None and tree.right is None:
        return [str(tree.entry)], len(str(tree.entry))//2
    num_width = len(str(tree.entry)) #Width of this tree's entry
    #If only right child:
    if tree.left is None:
        r_block, r_cent = tree_block(tree.right)
        #Add left padding if necessary
        if r_cent < num_width*3/2:
            padding = ' '*((num_width*3)//2-r_cent)
            r_cent += ((num_width*3)//2-r_cent) #Record new center
            for line_index in range(len(r_block)):
                r_block[line_index] = padding+r_block[line_index]
 
        #Generate top two lines
        t_line = str(tree.entry)
        t_line += '-'*(r_cent-len(t_line))
        t_line += ' '*(len(r_block[0])-len(t_line))
        m_line = ' '*r_cent + '\\'
        m_line += ' '*(len(r_block[0])-len(m_line))
 
        return [t_line, m_line]+r_block, num_width//2
    #If only left child:
    if tree.right is None:
        l_block, l_cent = tree_block(tree.left)
        #Add right padding if necessary
        if len(l_block[0]) < l_cent+1+num_width:
            padding = ' '*(l_cent+1+num_width-len(l_block[0]))
            for line_index in range(len(l_block)):
                l_block[line_index] = l_block[line_index]+padding
        #Generate lines
        t_line = ' '*(l_cent+1)
        t_line += '-'*(len(l_block[0])-l_cent-1-num_width)
        t_line += str(tree.entry)
        m_line = ' '*l_cent+'/'
        m_line += ' '*(len(l_block[0]) - len(m_line))
        return [t_line, m_line]+l_block, len(t_line)-num_width//2
    #Otherwise, has both
    l_block, l_cent = tree_block(tree.left)
    r_block, r_cent = tree_block(tree.right)
 
    #Pad left block
    spacing = r_cent+len(l_block)-l_cent-2
    padding = ' '*max(1, (spacing-num_width))
    for line_index in range(len(l_block)):
        l_block[line_index] = l_block[line_index]+padding
 
    #Add left and right blocks
    new_block = []
    for line_index in range(max(len(l_block), len(r_block))):
        new_line = l_block[line_index] if line_index < len(l_block) else ' '*len(l_block[0])
        new_line += r_block[line_index] if line_index < len(r_block) else ' '*len(r_block[0])
        new_block.append(new_line)
    r_cent += len(l_block[0])
 
    #Generate top lines
    my_cent = (l_cent+r_cent)//2
    t_line = ' '*(l_cent+1)
    t_line += '-'*(my_cent-num_width//2-len(t_line))
    t_line += str(tree.entry)
    t_line += '-'*(r_cent-len(t_line))
    t_line += ' '*(len(new_block[0])-len(t_line))
 
    m_line = ' '*l_cent + '/'
    m_line += ' '*(r_cent-len(m_line)) + '\\'
    m_line += ' '*(len(new_block[0])-len(m_line))
 
    return [t_line, m_line]+new_block, my_cent
"""
t = BinTree(6, BinTree(2, BinTree(0), BinTree(4)), BinTree(10, BinTree(8), BinTree(12)))
print(t)
"""    