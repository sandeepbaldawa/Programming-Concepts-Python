# A. In LRU we evict the Least recently used node and replace it with the most recently used if cache is full else insert 
# the same in cache
# B. Ordering is important to know the Least recently used node

# *IMPORTANT*
# Questions to Clarify: 
# Q. What should we return if an entry wasn't found? A. Return null
# 
# Say we want to add an entry (memory block) A to the cache. If the cache is not full, we simply add the entry. 
# If the cache is full, we need to make space. We remove the entry that was accessed 
# least recently (lets call this LR).This makes space, and now we can put A into the cache.
# We need to store cache entries in order of when they were accessed. So if entry X was read a second ago,it should be 
# at the front of our order. Same goes for entries that were added recently. If we keep blocks in this order, we can easily
# find the least recently used (LRU) element. Itshould just be last on the list. It is also important to access each block 
# quickly. It is a cache after all. So, we needa data structure that has the O(1) access of a hash table and keeps nodes 
# in order.Remember, in a hash table, keys are not stored in order.A Linked Hash Table is the best data structure for this. 
# It is a Linked List where each Nodeis stored in a Hash table as well.

# The cache will have the following 2 standard 
# operations:
# 1. read(key)
# 2. write(key, value). 
# You should check with the interviewer if they want other operations. When we read an entry in the middle of the linked list, 
# it becomes recently used. Sowe move it up to the front of the list. To move the node to front in O(1) time, we needto use a 
# doubly linked list. This is because as we need to remove the node from the listbefore adding it to front. As we saw earlier, 
# removal cannot be done in a singly linked list without the previous node.

# 1. LinkedList finding a node is O(N)
# 2. Order in HashTable is absent, but lookup is O(1)
# 3. We can combine Linkedlists and HasTables to get the best of both worlds

# *IMPORTANT*
# Pseudocode:
# write(key, value)
#  if full:     
#    Remove LRU Node 
#  add Node to front
# 
# read(key) 
#  remove node add node back to the front 
#  return node's value

# *IMPORTANT*
# Test Cases:
# Edge Cases: Null Node, 
# Empty Data structureBase Cases: Single element in Linked Hash Table
# Regular Cases: Read/Write, Cache Full/Empty/Not Full

# Time Complexity: O(1) for both reads and writes
# Space Complexity: O(n) where n is amount of data in cache

class Node:
def __init__(self, k, v):
    self.key = k
    self.val = v
    self.prev = None
    self.next = None

class LRUCache:
def __init__(self, capacity):
    self.capacity = capacity
    self.dic = dict()
    self.head = Node(0, 0)
    self.tail = Node(0, 0)
    self.head.next = self.tail
    self.tail.prev = self.head

def get(self, key):
    if key in self.dic:
        n = self.dic[key]
        self._remove(n)
        self._add(n)
        return n.val
    return -1

def set(self, key, value):
    if key in self.dic:
        self._remove(self.dic[key])
    n = Node(key, value)
    self._add(n)
    self.dic[key] = n
    if len(self.dic) > self.capacity:
        n = self.head.next
        self._remove(n)
        del self.dic[n.key]

def _remove(self, node):
    p = node.prev
    n = node.next
    p.next = n
    n.prev = p

def _add(self, node):
    p = self.tail.prev
    p.next = node
    self.tail.prev = node
    node.prev = p
    node.next = self.tail
