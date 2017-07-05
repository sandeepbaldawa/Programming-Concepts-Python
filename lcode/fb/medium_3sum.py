'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in xrange(len(nums)-2):
            # remove duplicate
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    res.append((nums[i],nums[left],nums[right]))
                    left += 1
                    # remove duplicate
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif sum < 0:
                    left += 1
                else:
                    right += -1
        return res 
