'''
You’re testing a new driverless car that is located at the Southwest (bottom-left) corner of an n×n grid. The car is 
supposed to get to the opposite, Northeast (top-right), corner of the grid. Given n, the size of the grid’s axes,
write a function numOfPathsToDest that returns the number of the possible paths the driverless car can take.
alt the car may move only in the white squares

For convenience, let’s represent every square in the grid as a pair (i,j). 
The first coordinate in the pair denotes the east-to-west axis, and the second coordinate denotes the south-to-north axis.
The initial state of the car is (0,0), and the destination is (n-1,n-1).
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
