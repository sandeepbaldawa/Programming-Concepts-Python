'''
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, 
"pwke" is a subsequence and not a substring.
'''
'''
1. Add all unique elements to a set
2. While adding if we find dup i.e. number already in set
   we keep deleting all numbers in the order of their addition till we reach
   the dup number i.e. if we have xyzabcaefg
   When we reach the dupe "a" we delete x,y,z and also a from the hashset, and also the window of consideration of max_len
   else we will have dupes(which question does not allow in a substring)
3. Everytime when we have a non-dupe element, calculate the max_len of the subtring  
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash_set, head, max_len = set(), 0, 0
        for idx, val in enumerate(s):
            while(val in hash_set):
                hash_set.remove(s[head])
                head += 1
            hash_set.add(val)
            max_len = max(max_len, idx-head+1)
        return max_len
