class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        
def reverse_ll(root):
    if not root or not root.next:
        return root
    
    curr = reverse_ll(root.next)
    root.next.next = root
    root.next = None
    return curr

def print_ll(root):
    while(root):
        print root.val
        root = root.next

dummy = root = Node(0)        
for i in xrange(1,11):
    root.next = Node(i)
    root = root.next

print_ll(dummy) 
rev = reverse_ll(dummy)
print_ll(rev)
