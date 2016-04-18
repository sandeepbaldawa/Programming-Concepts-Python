'''
Your task is to implement this first step and convert a given array of integers into a heap. You will
do that by applying a certain number of swaps to the array. Swap is an operation which exchanges
elements ai and aj of the array a for some i and j. You will need to convert the array into a heap
using only O(n) swaps, as was described in the lectures. 

Input:
5
5 4 3 2 1
Output:
3
1 4
0 1
1 3


'''


#!/usr/bin/python
# -*- coding: utf-8 -*-
# python3


class HeapBuilder:

    def __init__(self):
        self._swaps = []
        self._data = []

    def ReadData(self):
        self.n = 5  # int(input())
        self._data = [5, 4, 3, 2, 1]  # [int(s) for s in input().split()]
        assert self.n == len(self._data)

    def WriteResponse(self):
        print len(self._swaps)
        for swap in self._swaps:
            print (swap[0], swap[1])

    def GenerateSwaps(self, i):
        l = 2 * i + 1
        r = 2 * i + 2

      # print(l,r,self.n)

        smallest = i
        if l < self.n and self._data[l] < self._data[i]:
            smallest = l

        if r < self.n and self._data[r] < self._data[smallest]:
            smallest = r

        if smallest != i:
            self._swaps.append((i, smallest))
            (self._data[i], self._data[smallest]) = \
                (self._data[smallest], self._data[i])
            self.GenerateSwaps(smallest)

    def GenerateSwaps1(self):

    # The following naive implementation just sorts
    # the given sequence using selection sort algorithm
    # and saves the resulting sequence of swaps.
    # This turns the given array into a heap,
    # but in the worst case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation

        for i in range(len(self._data)):
            for j in range(i + 1, len(self._data)):
                if self._data[i] > self._data[j]:
                    self._swaps.append((i, j))
                    (self._data[i], self._data[j]) = (self._data[j],
                            self._data[i])

    def Solve(self):
        self.ReadData()
        for i in range(self.n - 1 // 2, -1, -1):
            self.GenerateSwaps(i)
        print self._data
        self.WriteResponse()


__name__ = '__main__'
if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()

			
