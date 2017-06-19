class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

class StackOfStrings():
    def __init__(self):
        self.first = None

    def push(self, item):
        '''Add at the head with new value'''
        new_node = Node(item)
        new_node.next = None
        if self.isEmpty():
            self.first = new_node
        else:
            new_node.next = self.first
            self.first = new_node

    def pop(self):
        '''Remove from the head and return value'''
        pop_item = None
        if not self.isEmpty():
            pop_item = self.first
            self.first = self.first.next
            return pop_item.val
        return pop_item

    def isEmpty(self):
        return self.first == None

s = StackOfStrings()
s.push(5)
assert s.pop() == 5
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
assert s.pop() == 5
assert s.pop() == 4
assert s.pop() == 3
assert s.pop() == 2
assert s.pop() == 1
assert s.pop() == None
