class Solution(object):
    def maxstock(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_so_far = float('inf')
        max_Diff = -float('inf') - 1
        for i in range(0, len(nums)):
            min_so_far = min(nums[i], min_so_far)
            max_Diff = max(nums[i]-min_so_far, max_Diff)
        return max_Diff

mySol = Solution()
nums=[2,1000000,3,500,100,1000]
print mySol.maxstock(nums)
