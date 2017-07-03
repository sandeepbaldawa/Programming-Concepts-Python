'''
Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.

Note:
If n is the length of array, assume the following constraints are satisfied:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)
Examples:

Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.

'''

''' dp solution '''

import sys
class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        dp = [[sys.maxint]*(m) for _ in range(len(nums)+1)]
        acc = 0
        dp[0][0] = 0
        for i in range(1, len(nums)+1):
            acc += nums[i - 1]
            dp[i][0] = acc

        for j in range(m):
            dp[0][j] = 0

        for i in range(1, len(nums)+1):
            for i_ in range(i):
                for j in range(1, m):
                    dp[i][j] = min(dp[i][j], max(dp[i_][j-1], dp[i][0]-dp[i_][0]))
        #print dp
        return dp[len(nums)][m-1]


''' Binary Search '''
class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        def valid(mid):
            cnt = 0
            current = 0
            for n in nums:
                current += n
                if current>mid:
                    cnt += 1
                    if cnt>=m:
                        return False
                    current = n
            return True

        l = max(nums)
        h = sum(nums)

        while l<h:
            mid = l+(h-l)/2
            if valid(mid):
                h = mid
            else:
                l = mid+1
        return l
