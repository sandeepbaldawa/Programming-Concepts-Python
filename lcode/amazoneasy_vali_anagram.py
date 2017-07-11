'''
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?

Can also use Counter

Using sorted might become costly for lot of elements.
'''

from collections import defaultdict
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict_s, dict_t = defaultdict(int), defaultdict(int)
        for each in s:
            dict_s[ord(each) - ord('a')] += 1
            
        for each in t:
            dict_t[ord(each) - ord('a')] += 1
            
        return dict_s == dict_t    
        
        
        
