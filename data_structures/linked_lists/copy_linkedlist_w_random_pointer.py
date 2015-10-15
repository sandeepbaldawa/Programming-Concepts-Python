1st Method
---------------
Create a HashMap of Key/val corresponding to the node addresses in new and old linked_list in first pass
Then in second pass link the random nodes using row in the HashMap

2nd Method
---------------
Inser new nodes in between the old linked list with old linked list pointing to new nodes.
p1.next.random = p1.random.next

