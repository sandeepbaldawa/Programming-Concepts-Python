'''
Find duplicates nums[i] == nums[j]
given (i - j) < K
'''

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dict = {}
        for i, val in enumerate(nums):
            if val in dict.keys() and abs(i - dict[val]) <= k:
                return True
            dict[val] = i
        return False
