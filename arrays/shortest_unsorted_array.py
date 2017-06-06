'''
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.
'''

class Solution(object):
    def findUnsortedSubarray(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(arr) <= 0:
            return None
        
        begin, end = -1, -2 # Important if array is already sorted
        max_arr = float('-inf')
        min_arr = float('inf')
        n = len(arr)
        for i, val in enumerate(arr):
            max_arr = max(max_arr, arr[i])
            min_arr = min(min_arr, arr[n-i-1])
            if arr[i] < max_arr: # Find if any element is lesser than maxsoFar, that becomes your end
                end = i 
            if arr[n-i-1] > min_arr: # Find if any element is greater than minsoFar, that becomes your start
                begin = n-i-1 
        return end - begin + 1       
                
            
