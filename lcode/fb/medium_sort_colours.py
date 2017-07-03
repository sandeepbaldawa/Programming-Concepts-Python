'''
Given an array with n objects colored red, white or blue, sort them so that objects of the 
same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
'''
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        smaller, equal, larger, pivot = 0 , 0, len(nums), 1
        while(equal < larger):
            if nums[equal] == pivot:
                equal += 1
            elif nums[equal] < pivot:
                nums[smaller], nums[equal] = nums[equal], nums[smaller]
                smaller, equal = smaller+1, equal + 1
            elif nums[equal] > pivot:
                larger -= 1    
                nums[larger], nums[equal] = nums[equal], nums[larger]
                 
                
        
        
