"""
LETTERPHONE

Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.



The digit 0 maps to 0 itself.
The digit 1 maps to 1 itself.

Input: Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Make sure the returned strings are lexicographically sorted.

"""
dict = { '1': "1",
      '2': "abc",
      '3': "def",
      '4': "ghi",
      '5': "jkl",
      '6': "mno",
      '7': "pqrs",
      '8': "tuv",
      '9': "wxyz",
}

res = []
def pressingButtons(buttons):
    if len(buttons) <= 0:
        return res
    helper(buttons, 0, "")
    return res
    

def helper(buttons, i, soFar=""): 
   if i >= (len(buttons)):
       res.append(soFar)
       return
    
   for val in dict[buttons[i]]:
        helper(buttons, i+1, soFar + val)
