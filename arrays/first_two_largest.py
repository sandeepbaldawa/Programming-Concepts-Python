import unittest
import random


def two_biggest(A):
   """ Method which finds first and second largest nos
   Returns int, int"""

   first_big = -float('INF')
   second_big = -float('INF')
 
   # exit if less elements
   if len(A) < 2:
      return -1, -1 

   # find first and second largest
   for i in range(len(A)):
       if A[i] > first_big:
          second_big = first_big
          first_big = A[i]
       elif A[i] < first_big and A[i] > second_big:
          second_big = A[i]
   return first_big, second_big     
   
class test_two_biggest(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_smoke(self):
        a = [1,2,3,4,5]
        assert(two_biggest(a) == (5, 4))
 
    def test_smoke_extended(self):
        a = [-1,-2,-3,-4,-5]
        assert(two_biggest(a) == (-1, -2))

    def test_mix(self):
        a = [-1,-2,-3,4,5]
        assert(two_biggest(a) == (5, 4))

    def test_empty(self):
        a = []
        assert(two_biggest(a) == (-1, -1))
    
    def test_(self):
        a = []
        assert(two_biggest(a) == (-1, -1))

    def test_long(self):
        a = []
        for i in range(10000000):
            a.append(i)  
        assert(two_biggest(a) == (9999999, 9999998))

    def test_random(self):
        for j in range(100):
            a = []
            till = int(random.random() * 1000000)
            max_1 = till - 1 
            max_2 = till - 2 
            for i in range(till):
                a.append(i)  
            assert(two_biggest(a) == (max_1, max_2))


if __name__ == '__main__':
    unittest.main()
