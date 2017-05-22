'''
Find paths to go from 0,0 to n-1, n-1 in a square grid
using unoptimized recursion
This can be further improved by memoization and even further improved by 
bottom up approach using DP..

Complexity O(2^N)
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


'''
Using DP 

Complexity O(N^2)
'''
def numOfPathsToDest(n):
    if n <= 1:
      return n
    a = [[0]*(n+1) for _ in range(n+1)]
    for i in range(n+1):
       a[0][i] = 1

    for i in range(n+1):
       for j in range(n+1):
          if i >= j and i > 0 and j > 0:
             a[i][j] = a[i-1][j] + a[i][j-1]
    return a[n][n]

print numOfPathsToDest(4)
