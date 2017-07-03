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
