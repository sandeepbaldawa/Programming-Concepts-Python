
class StackOfStrings():
    def __init__(self, capacity):
        self.stack = [0] * capacity
        self.stack_idx = 0

    def push(self, item):
        '''Add at the head with new value'''
        self.stack[self.stack_idx] = item
        self.stack_idx += 1

    def pop(self):
        '''Remove from the head and return value'''
        print self.stack_idx
        if self.stack_idx > 0:
            self.stack_idx -= 1
            return self.stack[self.stack_idx]
        else:
            return None

    def isEmpty(self):
        return self.stack_idx == 0

s = StackOfStrings(5)
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
