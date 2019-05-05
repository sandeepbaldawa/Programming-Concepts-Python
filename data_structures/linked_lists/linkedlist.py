class linkedlist:
   """
   LinkedList Node
   """ 
   def  __init__(self, data):
        self.data = data
        self.next = None

def print_ll(head):
    """
    Print Linked List
    """
    tmp = head
    while(tmp):
        print tmp.data 
        tmp = tmp.next
    print("\n")

def find_circular(root):
    """
    1. Check if linked list is circular
    2. Length of cycle is the point the slow, fast meet, increment 
    slow till it reaches the same point again
    """
    if not root or not root.next:
        return None
    slow = root
    fast = root.next
    while(fast and fast.next):
        if (slow == fast):
            print "Is Circular"
            return True
        slow = slow.next
        fast = fast.next.next
    return False

def find_median(root):
    if not root or not root.next:
        return None
    slow = root
    fast = root.next
    while(fast and fast.next):
        slow = slow.next
        fast = fast.next.next
    return slow

def find_3rdlast_node(root):
    if not root or not root.next:
        return None
    slow = root
    fast = root.next.next # start fast pointer from 3rd node
    while(fast and fast.next):
        slow = slow.next
        fast = fast.next
    return slow

def rev(root):
    """
    Reverse linked list non-recursive
    """
    prev = None
    curr = root
    next = curr.next
    while(curr and curr.next): 
        curr.next = prev
        prev = curr
        curr = next
        next = curr.next
    curr.next = prev
    return curr

def rev_recur(root):
   """
   Reverse linked list recursive
   """
   if not root.next:
       return root

   curr = rev_recur(root.next)
   curr.next = root
   root.next = None
   return root

def reverse_ll_optimized(root):
   """
   Reverse linked list recursive optimized
   https://github.com/sandeepbaldawa/Programming-Concepts-Python/blob/master/data_structures/linked_lists/reverse.py
   """ 
   if not root or not root.next:
       return root
    
   curr = reverse_ll_optimized(root.next)
   root.next.next = root
   root.next = None
   return curr



   
def split_ll(root):
    """
    Split the linked list
    1. Find the mid node
    2. Assign mid->next as None
    3. Create head of second list from mid->next till end
    """
    if not root or not root.next:
        return None
    slow = root
    fast = root.next
    while(fast and fast.next):
        slow = slow.next
        fast = fast.next.next
   
    l2_head = slow.next 
    slow.next = None 
    #print_ll(root
    #print_ll(l2_head)
    #print " Mid is ", slow.data
    return l2_head

def move(dest, src):
    tmp = src.next
    src.next = dest
    dest = src
    src = tmp

def shuffle_merge(l1, l2):
    """
    Combine first node from l1 and one node from l2 and then
    second node from l1 and second node from l2 and so on..
    Technique in standford linkedlist document
    - Use dummy node as the starting node
    - 
    """
    tail = linkedlist(9)
    dummy = tail 
    while(True):
        if not l1:
            tail.next = l2
            break 
        if not l2:
            tail.next = l1
            break  

        tail.next = l1
        tail = tail.next
        l1 = l1.next  

        tail.next = l2
        tail = tail.next
        l2 = l2.next

    return dummy.next 

    
    
def merge_optimized(n1, n2):
    """
    Optimized merge sort using linked list and
    dummy node at the start for merging, makes it
    pretty simple to merge
    """
    def mergeTwoLists(l1, l2):
            curr = dummy = ListNode(0)
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            curr.next = l1 or l2
            return dummy.next

def split_even_odd(l):
    """
    Splits a given linkedlist into even elements and odd elements
    Uses dummy nodes to maintain the head of the two linked lists
    """
    tail1 = linkedlist(9)
    dummy1 = tail1 
    tail2 = linkedlist(9)
    dummy2 = tail2 
    curr = l 
    #print curr
    while(curr):
        if((curr.data % 2) == 0):
            tail1.next = curr
            tail1 = curr
        else:
            tail2.next = curr
            tail2 = curr
        curr=curr.next     

    return (dummy1.next, dummy2.next)
 
def merge(n1, n2):
    if (n1.data <= n2.data):
        tmp = linkedlist(n1.data)
        n1 = n1.next
    else:
        tmp = linkedlist(n2.data)
        n2 = n2.next
    m_list = tmp
    head = m_list 

    while (n1 and n2):
        if (n1.data <= n2.data):
            tmp = linkedlist(n1.data)
            m_list.next = tmp 
            n1 = n1.next
        else:
            tmp = linkedlist(n2.data)
            m_list.next = tmp 
            n2 = n2.next
        m_list = m_list.next
    
    while(n1):
        tmp = linkedlist(n1.data)
        m_list.next = tmp 
        n1 = n1.next
        m_list = m_list.next

    while(n2):
        tmp = linkedlist(n2.data)
        m_list.next = tmp 
        n2 = n2.next
        m_list = m_list.next
    m_list.next = None
    return head 


         
def mergesort(node):
    if not node.next :
        return node
    mid = split_ll(node)
    #print_ll(node)
    #print_ll(mid)
    n1 = mergesort(node)
    n2 = mergesort(mid)
    return merge_optimized(n1, n2)
   
input = [1, 3, 20, 32, 5, 7, 64, 8]
input1 = [400, 355, 240, 342, 455, 457, 464, 548]
#input = []
#input = [2]
head = linkedlist(9)
curr = head
for each in input:
    curr.next = linkedlist(each)
    curr = curr.next

curr.next = None  

head1 = linkedlist(9)
curr = head1
for each in input1:
    curr.next = linkedlist(each)
    curr = curr.next

curr.next = None  

#print_ll(head)
#find_circular(head)
#split_ll(head)    
#print_ll(head)
#tmp = head
#while(tmp.next):
#    tmp = tmp.next
#print "********************\n"
#print tmp.data
#print "********************\n"
#
#my_rev = rev_recur(head)    
print_ll(head)
#print_ll(head1)
#tmp = mergesort(head)
#print_ll(tmp)
(even,odd) = split_even_odd(head)
print_ll(even)
print_ll(odd)
#print_ll(odd)

#res = shuffle_merge(head, head1)
#print_ll(res)
