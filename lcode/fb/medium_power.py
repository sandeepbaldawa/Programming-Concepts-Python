'''
Brute force is doing a x*x*x*x..n which takes O(2^N) where N is number of bits needed to represent x

For optimizing 
if LSB of x is 0(product of "2") then result is (x^n/2)^2 else result is x * (x^n/2)^2
Also x^(y0 + y1) = x^y0 * x^y1

eg:-
x^9 = x^(1010) = x^101 * x^101 
x^101 = x^100 * x = x^10 * x^10 * x

x 9      9*9  9*9*9  9*9*9*9*9*9   
n 1010   101  10        1
'''
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        result = 1.0
        if n < 0:
            n, x = -n, 1.0/x
            
        while n:
            if n & 1:
                result *= x
            x, n = x*x, n >> 1
        return result    
