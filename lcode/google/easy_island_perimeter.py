'''
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:

[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16

Solution idea:- If neighbour is "0" or nrighbour is end of matrix grid then it is counted as perimeter
'''
class Solution(object):
    def islandPerimeter(self, arr):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        peri = 0
        row_len, col_len = len(arr), len(arr[0])
        for row in xrange(row_len):
            for col in xrange(col_len):
                if arr[row][col] == 1:
                    if col-1 < 0 or arr[row][col-1] == 0:
                        peri += 1
                    if col+1 >= col_len or arr[row][col+1] == 0:
                        peri += 1  
          
                    if row-1 < 0 or arr[row-1][col] == 0:
                        peri += 1
                    if row+1 >= row_len or arr[row+1][col] == 0:
                        peri += 1
        return peri
