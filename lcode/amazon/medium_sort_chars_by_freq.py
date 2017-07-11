'''
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"
'''

from collections import defaultdict
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = defaultdict(int)
        for each in s:
            res[each] += 1
        
        res = sorted(res.items(), key = lambda i: i[1], reverse=True)
        return "".join([key*val for key,val in res])
