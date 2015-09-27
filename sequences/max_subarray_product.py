class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_product = nums[0]
        curr_min = curr_max = 1
        for i in range(0, len(nums)):
            curr_min, curr_max = min(nums[i], curr_min * nums[i], curr_max * nums[i]), max(nums[i], curr_min * nums[i], curr_max * nums[i])
            max_product = max(max_product,curr_max)
        return max_product
