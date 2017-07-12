'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
'''

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {1:[],2:[]}
        for idx, val in enumerate(s):
            if val in dict[1]:
                dict[2].append(val)
            else:
                dict[1].append(val)
        
        for idx, val in enumerate(s):
            if val in dict[1] and val not in dict[2]:   
                return idx
        return -1   
        
