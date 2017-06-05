'''
No which occurs more that N/2 of the size of the array

1. Counting method
T - O(N^2)
S - O(1)

2. Sorting method
T -  O(N logN)
S -  O(1)

3. Hashing method
T -  O(N)
S -  O(N)

4. Canceling method
2 2 1 4 2 5 2

If same number replace by it
If different cancel it..

2 - - 2

T - O(N)
S - O(N)

5. Voting method
T - O(N)
S - O(1)

6. Median element
Find median of an error

7. Randomized method
T - O(logN)
S - O(logN)
p = 1- 1/n

'''
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate, count = None, 0   
        for each in nums:
            if count == 0:
                candidate = each
                count += 1
            elif candidate == each:
                count += 1
            else:
                count -= 1
        
        return candidate
