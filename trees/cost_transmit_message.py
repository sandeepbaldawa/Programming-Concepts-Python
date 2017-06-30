'''
Find total time taken to transmit a message, at a give time t1 any node can send message
to only one child. and in time t2 to it's other child, t3 to third child and so on...
A node cannot start transmitting a message until it has received the message.
Write a function to calculate the cost to transmit a message from a root node to all the leaf children.
This is a n-ary tree.
'''

from collections import deque
class Node(object):
    def __init__(self, val):
        self.val = val
        self.child = list()

def get_cost_transmit(root):
    ''' Get cost of trasmitting message from root to leaf nodes
    Each queue element is a tuple i.e. (node_addr, time_stamp_transmitted)
    '''
    if not root:
        return 0

    q, curr_time, max_time = deque(), 0, -1
    q.append((root, curr_time))
    while(len(q) > 0):
        curr_node, curr_time = q.pop()
        for each_child in curr_node.child:
            curr_time += 1
            q.append((each_child, curr_time))
            max_time = max(max_time, curr_time)
            get_cost_transmit(each_child)
    return max_time


root = Node(100)
root.child.append(Node(50))
root.child.append(Node(100))
assert get_cost_transmit(root) == 2

root = None
assert get_cost_transmit(root) == 0

r = Node(100)
r_c1 = r.child.append(Node(50))
r_c2 = r.child.append(Node(150))
r_c3 = r.child.append(Node(250))
assert get_cost_transmit(r) == 3
