"""
Given an unsorted integer array, find the first missing positive integer.
For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.
Your algorithm should run in O(n) time and uses constant space.
"""

"""
Idea
------
The idea is as follow:
e.g. 3,2,5,1,7
For each element,
1. Do not consider the element which <=0, or value > length n
2. Swap this element A[i] with the A[A[i]-1], e.g. when we met A[0]=3, we swap A[0] and A[2], then A[0]=5
3. For the current element A[i], if A[i]<=0 or A[i]>length n, or A[i] has already occurred, break. Else go to step 2.
    e.g. A[0]=5, swap A[0] and A[5], A[0]=7, break.Now the array A is {7,2,3,1,5}.
    Next round, A is {1,2,3,7,5}
4. Scan the array A and find the result. e.g. {1,2,3,7,5}, the A[3]!=3+1, print 3+1, result =4.
"""

