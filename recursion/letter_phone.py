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
# Tail recursion
d = { '1': "1",
      '2': "ABC",
      '3': "DEF",
      '4': "GHI",
      '5': "JKL",
      '6': "MNO",
      '7': "PQRS",
      '8': "TUV",
      '9': "WXYZ",
}

def getphoneMneumonicHelper(input, digitIndex, acc):
	if digitIndex < len(input):
		digit = input[digitIndex]
		for c in d[str(ord(input[digitIndex]) - ord('0'))]:
			acc[digitIndex] =  c
			getphoneMneumonicHelper(input, digitIndex + 1, acc)
	else:
		print acc
	
acc = [None] * 3
getphoneMneumonicHelper("567", 0 , acc)
