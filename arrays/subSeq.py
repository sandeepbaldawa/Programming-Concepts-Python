""""
     * PROBLEM DEFINITION CREDIT: InterviewBit.com
     *
     * Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
     *
     * For example:
     * Given the array [-2,1,-3,4,-1,2,1,-5,4],
     * the contiguous subarray [4,-1,2,1] has the largest sum = 6.
     * For this problem, return the max sub array.
     *
     * SOLUTION: 
     *
     * @param arr
     * @return
"""


#!/usr/bin/python
# -*- coding: utf-8 -*-


def maxContiguousSubArray(arr):
    maxSumSoFar = -float('INF') - 1
    prefixSum = 0
    maxStart = 0
    maxEnd = 0
    for i in range(len(arr)):
        prefixSum = prefixSum + arr[i]
        print prefixSum, arr[i]
        if prefixSum > maxSumSoFar:
            maxSumSoFar = prefixSum
            maxEnd = i
        if prefixSum < 0:
            prefixSum = 0
            maxStart = i + 1

    print arr[maxStart:maxEnd + 1]

arr = [-2,1,-3,4,-1,2,1,-5,4]   
maxContiguousSubArray(arr)    
