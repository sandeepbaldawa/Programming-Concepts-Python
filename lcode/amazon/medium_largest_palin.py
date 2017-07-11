'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
Example:

Input: "cbbd"

Output: "bb"
'''

class Solution(object):
    def longestPalindrome(self, text):
        """
        :type s: str
        :rtype: str
        """
        
        if len(text) <= 1:
            return text
        items=[]
        "Return (i, j) such that text[i:j] is the longest palindrome in text."
        for start in range(len(text)):
            for end in (start, start+1):
                items.append(self.grow(text,start,end))
        return self.max_diff(text, items)
   
    def length(self, slice):
        a,b = slice
        return b-a
    
    def grow(self, text, start, end):
        while (start > 0 and end < len(text) and text[start-1].lower() == text[end].lower()):
            start -= 1
            end += 1
        return (start, end)    

    def max_diff(self, text, items):
        maxsoFar, s_i ,e_i = 0, 0 , 0
        for s, e in items:
            if e-s > maxsoFar:
                s_i, e_i = s, e 
                maxsoFar = e-s
        return text[s_i:e_i]  
