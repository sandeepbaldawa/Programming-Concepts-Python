class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if len(digits) <= 0:
            return digits
        
        #Add one to end of the array
        digits[-1] += 1    
        
        for i in reversed(range(1, len(digits))):
            if digits[i] != 10:
                break
            
            digits[i] = 0
            digits[i-1] += 1
        
        if digits[0] == 10:
            digits[0] = 0
            digits.insert(0, 1)
        
        return digits    
            
