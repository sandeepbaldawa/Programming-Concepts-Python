'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
'''

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.stack or len(self.stack) == 0:
            self.stack.append(x)
            self.min.append(x)
            return
        self.stack.append(x)
        self.min.append(min(self.min[-1], x))
        

    def pop(self):
        """
        :rtype: void
        """
        if not self.stack or len(self.stack) == 0:
            return
        val = self.stack.pop()
        self.min.pop()
        return val
        

    def top(self):
        """
        :rtype: int
        """
        if not self.stack:
            return
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if not self.min or len(self.min) == 0:
            return
        return self.min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
