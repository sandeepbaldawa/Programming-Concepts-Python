"""
You are playing the following Flip Game with your friend: Given a string that contains 
only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--". 
The game ends when a person can no longer make a move and therefore the other person will be the winner.
Write a function to determine if the starting player can guarantee a win.
For example, given s = "++++", return true. The starting player can guarantee a win by flipping the middle "++" to become "+--+".
"""
class Solution(object):
    def __init__(self):
        self.dict = {}

    def canWin(self, s):
        if s in self.dict:
            return self.dict[s]
        result = False
        for i in range(len(s)-1):
            if s[i:i+2] == "++" and not self.canWin(s[:i] + "--" + s[i+2:]):
                result = True
                break
        self.dict[s] = result
        return result
sol = Solution()
print sol.canWin("++++++")
print sol.canWin("++")
