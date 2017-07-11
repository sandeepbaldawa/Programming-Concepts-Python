'''
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.



Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
'''

class Solution(object):
    def __init__(self):
        self.res = []
        self.dict = {'1':"",'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz",'0':""}
        
        
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return self.res
        self.helper(digits, 0, "")
        return self.res
    
    def helper(self, digits, idx, acc):
        if idx == len(digits):
            self.res.append(acc)
            return
        
        for each_map in self.dict[digits[idx]]:
            self.helper(digits, idx+1, acc+each_map)
    
   
