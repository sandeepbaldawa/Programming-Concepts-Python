"""
Given an unsorted integer array, find the first missing positive integer.
For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.
Your algorithm should run in O(n) time and uses constant space.


Note: numbers A[i]<=0 and A[i]>N ( N being the size of the array ) is not important to us since the missing positive integer will be in the range [1, N+1].

The answer will be N+1 only if all of the elements of the array are exact one occurrence of [1, N].

Creating buckets would have been an easy solution if using extra space was allowed.

An array of size N initialized to 0 would have been created.

For every value A[i] which lies in the range [1, N], its count in the array would have been incremented.

Finally, traversing the array would help to find the first array position with value 0 and that will be our answer. 
However, usage of buckets is not allowed, can we use the existing array as bucket somehow?

Now, since additional space is not allowed either, the given array itself needs to be used to track it.

It may be helpful to use the fact that the size of the set we are looking to track is [1, N]

which happens to be the same size as the size of the array.

This means we can use the array to track these elements.

We traverse the array and if A[i] is in [1,N] range, we try to put in the index of same value in the array.
"""

class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        for i in range(len(A)):
            if (A[i] > 0 and A[i] <= len(A)):
                pos = A[i] - 1
                if (A[pos] != A[i]):
                    A[pos], A[i] = A[i], A[pos]
                    i = i - 1
       
        for i in range(len(A)):
            if (A[i]!=(i+1)):
                return i+1
        return len(A)+1
