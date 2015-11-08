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

 /**
     * CREDIT: InterviewBit.com
     *
     * Find out the maximum sub-array of non negative numbers from an array.
     * The sub-array should be continuous.That is, a sub-array created by choosing
     * the second and fourth element and skipping the third element is invalid.
     * Maximum sub-array is defined in terms of the sum of the elements in the sub-array.
     * Sub-array A is greater than sub-array B if sum(A) > sum(B).
     *
     * Example:
     * A : [1, 2, 5, -7, 2, 3]
     * The two sub-arrays are [1, 2, 5] [2, 3].
     * The answer is [1, 2, 5] as its sum is larger than [2, 3]
     * NOTE: If there is a tie, then compare with segment's length and return segment which has maximum length
     * NOTE 2: If there is still a tie, then return the segment with minimum starting index
     *
     * @param input input array
     *
     * @return the maximum sub-array of non-negative numbers
     *
     */
