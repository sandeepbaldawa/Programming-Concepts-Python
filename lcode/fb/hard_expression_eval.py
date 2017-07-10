'''
Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

Examples: 
"123", 6 -> ["1+2+3", "1*2*3"] 
"232", 8 -> ["2*3+2", "2+3*2"]
"105", 5 -> ["1*0+5","10-5"]
"00", 0 -> ["0+0", "0-0", "0*0"]
"3456237490", 9191 -> []
'''

class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        self.res = []
        if num:
            self.helper(num, "", target)
        return self.res
     
    def helper(self, num, acc, target):   
        if not num:
    	    if eval(acc) == target:
    	        self.res.append(acc)
     
        for i in range(1, len(num)+1):
            if acc != "":
    	        self.helper(num[i:], acc + "+" + num[:i], target)
    	        self.helper(num[i:], acc + "-" + num[:i], target)
                self.helper(num[i:], acc + "*" + num[:i], target)
            else:
                self.helper(num[i:], num[:i], target)
