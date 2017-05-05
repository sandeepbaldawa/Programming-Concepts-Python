'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].
'''

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        curr, nz = 0, -1
        while(curr < len(nums)):
            if nums[curr] != 0:
                nz += 1
                nums[curr], nums[nz] = nums[nz], nums[curr]
            curr += 1
