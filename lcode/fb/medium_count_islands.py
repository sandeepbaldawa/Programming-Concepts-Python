'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3
'''

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or len(grid) <= 0:
            return 0
        
        self.visited = [[False]* (len(grid[0])) for _ in xrange(len(grid))]
        return self.helper(grid)
    
    def helper(self, grid):
        count = 0
        for row in xrange(len(grid)):
            for col in xrange(len(grid[0])):
                if grid[row][col] == '1' and not self.visited[row][col]:
                    self.explore(grid, row, col)
                    count += 1
        return count
    
    def is_invalid_index(self, grid, row, col):
        return row<0 or col<0 or row>=len(grid) or col>=len(grid[0]) or grid[row][col] != '1' or self.visited[row][col]
        
    def explore(self, grid, row, col):
        '''
        Run DFS here for each row and column index to find all
        neighbouring 1's
        :param arr:
        :param row:
        :param col:
        :return:
        '''
        # explore if 1 and not visited
        if self.is_invalid_index(grid, row, col):
            return
        self.visited[row][col] = True
        self.explore(grid, row - 1, col)
        self.explore(grid, row + 1, col)
        self.explore(grid, row, col - 1)
        self.explore(grid, row, col + 1)
        return
