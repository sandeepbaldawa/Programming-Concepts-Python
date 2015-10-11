class CircularBuffer:
        def __init__(self,size_max):
                self.max = size_max
                self.data = []
                self.head = 0
        def append(self,x):
                """append an element at the end of the buffer"""
                if len(self.data) == self.max:
                        self.head=0
                        self.data[self.head]=x
                        self.head=(self.head+1) % self.max
                else:
                    self.data.append(x)
        def get(self):
                """ return a list of elements from the oldest to the newest"""
                if len(self.data) == self.max:
                     return self.data[self.head:]+self.data[:self.head]
                return self.data


# sample of use
x=CircularBuffer(5)
x.append(1); x.append(2); x.append(3); x.append(4)
print "Get ", x.get()
x.append(5)
print " Append 5", x.get()
x.append(6)
print " Apppend 6 ", x.get()
x.append(7); x.append(8); x.append(9); x.append(10)
print "Get ",  x.get()
