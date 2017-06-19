class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

class QueueOfStrings():
    def __init__(self):
        self.first = None
        self.last = None

    def enqueue(self, item):
        '''Add at the tail with new value'''
        new_node = Node(item)
        new_node.next = None
        if self.isEmpty():
            self.first = self.last = new_node
        else:
            self.last.next = new_node
            self.last = self.last.next

    def dequeue(self):
        '''Remove from the head and return value'''
        deq_item = None
        if not self.isEmpty():
            deq_item = self.first
            self.first = self.first.next
            return deq_item.val
        return deq_item

    def isEmpty(self):
        return self.first == None

q = QueueOfStrings()
q.enqueue(5)
assert q.dequeue() == 5
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
assert q.dequeue() == 1
assert q.dequeue() == 2
assert q.dequeue() == 3
assert q.dequeue() == 4
assert q.dequeue() == 5
assert q.dequeue() == None
