'''
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
'''
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix or len(matrix) == 0:
            return matrix
        
        zero_rows = set()
        zero_cols = set()
        
        m, n = len(matrix), len(matrix[0])
        for row in xrange(m):
            for col in xrange(n):
                if matrix[row][col] == 0:
                    if row not in zero_rows:
                        zero_rows.add(row)
                    if col not in zero_cols:
                        zero_cols.add(col) 
         
        for r in zero_rows:
            for c in xrange(n):
                matrix[r][c] = 0
        
        for c in zero_cols:
            for r in xrange(m):
                matrix[r][c] = 0
                
        
