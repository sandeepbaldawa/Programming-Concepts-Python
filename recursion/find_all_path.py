'''
Find paths to go from 0,0 to n-1, n-1 in a square grid
using unoptimized recursion
This can be further improved by memoization and even further improved by 
bottom up approach using DP..
'''

def allpaths(x, y, n):
   if x > n-1 or y > n-1:
     return 0
   if x < y:
     return 0
   if x == n-1 and y == n-1:
      return 1
   print x,y
   m1 = allpaths(x+1, y, n)
   m2 = allpaths(x, y+1, n)
   return m1 + m2

print allpaths(0, 0, 4)
