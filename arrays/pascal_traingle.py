'''
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''

class Solution(object):
    def generate(self, rows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if rows <= 0:
            return []
        
        final_res = [[1]]
        if rows == 1:
            return final_res
        
        final_res = [[1],[1,1]]
        if rows == 2:
            return final_res
        
        for i in range(2, rows):
            curr_row_res, idx = [], 1
            curr_row_res.append(1) # Add 1 at start
            while(idx < len(final_res[i-1])):
                prev_row_second = final_res[i-1][idx]
                prev_row_first  = final_res[i-1][idx-1]
                curr_row_res.append(prev_row_second + prev_row_first)
                idx += 1
                
            curr_row_res.append(1) # Add 1 at end
            final_res.append(curr_row_res)
        return final_res
