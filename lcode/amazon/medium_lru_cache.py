class LRUCache:

  def __init__(self, capacity):
    self.capacity = capacity
    self.cache = {}
    self.cache_vals = LinkedList()

  def set(self, key, value):
    if self.cache.__contains__(key):
      print "exec"
      node = self.cache[key]
      node.data = value
      self.cache_vals.remove(node)
      self.cache_vals.insert_at_tail(node)
    else:
      self.evict_if_needed()
      node = LinkedListNode(key, value)
      self.cache_vals.insert_at_tail(node)
      self.cache[key] = node
  
  def get(self, key):
    if self.cache.__contains__(key):
      node = self.cache[key]
      self.cache_vals.remove(node)
      self.cache_vals.insert_at_tail(node)
      return node.data
    else:
      return -1

  def evict_if_needed(self):
    if self.cache_vals.size >= self.capacity:
      node = self.cache_vals.remove_head()
      del self.cache[node.key]

  def printcache(self):
    node = self.cache_vals.head
    while node != None :
      print str(node.key) + " " + str(node.data) + ", "
      node = node.next
