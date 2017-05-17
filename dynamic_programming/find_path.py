'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Variations:-
1. Some cells are walls, can't count that path 
2. Upper diagonal elements are not accessible. (i <= j elements)
'''

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0 or n == 0:
            return 0
            
        arr = [[0]*n for _ in range(m)]
        
        for i in range(m):
            arr[i][0] = 1
        
        for i in range(n):
            arr[0][i] = 1    
            
        for i in range(m):
            for j in range(n):
                   if(i > 0 and j > 0):
                      arr[i][j] = arr[i-1][j] + arr[i][j-1]
        return arr[m-1][n-1]        
        
