'''
Given a perfect binary tree, connect 
nodes from left to right at any given level

PS:- perfect binary tree is an important hint for the solution

Brute force:-
Take a queue and push all elements at a given level  in the queue
and then connect them, do this for all the levels
Time and Space are both O(N)

Can we do better?
Since it is a perfect binary tree
At level n if we have the root node
root.left.next = root.right  => this connect nodes at n+1 level

Now to conect nodes at n+2 level
     0      => n
   1   2    => n+1
 3  4 5  6  => n+2
  
  1.left.next = 1.right        (to connect 3=>4)
  1.right.next = 1.next.left  (to connect 4=>5)
  2.left.next = 2. right      (to connect 5=>6)  (This repeats so can be put in loop)

Time :- O(N)
Space :- O(1)
'''


class Node():
    def __init__(self):
        self.val, self.left, self.right = None
        self.next = None #Connect left to right
    
    def connect_all_levels(self, root):   
        '''Connects all nodes from all levels left to right'''
        def connect_all_at_some_level(self, node):
            '''Connects all nodes at a given level from left to right'''
            start_node = node
            while(start_node):
                start_node.left.next = start_node.right
                start_node.right.next = start_node.next.left
                start_node = start_node.next
        while(root.left):
            self.connect_all_levels(root)
            root = root.left
