'''
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?
'''

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for layer in range(n/2):
            first, last = layer, n-layer-1
            for i in range(first, last):
                offset = i - first
                
                # save top
                top = matrix[first][i]
                
                # left -> top
                matrix[first][i] = matrix[last - offset][first]
                
                # bottom -> left
                matrix[last - offset][first] = matrix[last][last - offset]
                
                # right -> bottom
                matrix[last][last - offset] = matrix[i][last]
                
                # top -> right
                matrix[i][last] = top
                
