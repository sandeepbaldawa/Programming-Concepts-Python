'''
Find count of all palindromes in substrings
'''
def isPalindrome(input, i , j):
   tmp = input[i:j+1]
   #print tmp
   return tmp ==  tmp[::-1]

# O(N^3)
def getPalindromes(input):
   count = 0
   for i in range(len(input)):
      for j in range(i, len(input)):
         if isPalindrome(input, i , j):
            count += 1

   return count

# O(N^2)
def getPalindromesOptimized(input):
   count = 0
   for i in range(len(input)):
      for j in range(len(input)):
         if (i-j) < 0 or ((i+j) >= len(input)):
           break
         if input[i+j] != input[i - j]:
            break
         else:
            count += 1

   for i in range(len(input)):
      for j in range(len(input)):
         if (i-j) < 0 or ((i+j+1) >= len(input)):
           break
         if input[i+j+1] != input[i - j]:
            break
         else:
            count += 1

   return count
input = "abbbba"
print getPalindromes(input)
print getPalindromesOptimized(input)

# --------------
# User Instructions
#
# Write a function, longest_subpalindrome_slice(text) that takes 
# a string as input and returns the i and j indices that 
# correspond to the beginning and end indices of the longest 
# palindrome in the string. 
#
# Grading Notes:
# 
# You will only be marked correct if your function runs 
# efficiently enough. We will be measuring efficency by counting
# the number of times you access each string. That count must be
# below a certain threshold to be marked correct.
#
# Please do not use regular expressions to solve this quiz!
def longest_subpalindrome_slice(text):
    if len(text) <= 1:
        return (0,len(text))
    items=[]
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    for start in range(len(text)):
        for end in (start, start+1):
            items.append(grow(text,start,end))
    return max_diff(items)
    
def grow(text, start, end):
    while (start > 0 and end < len(text) and text[start].lower() == text[end].lower()):
        start -= 1
        end += 1
    return (start, end)    

def max_diff(items):
    maxsoFar = 0
    s_i = e_i = 0
    for s, e in items:
        if e-s > maxsoFar:
            s_i, e_i = s, e 
            maxsoFar = e-s
    return s_i, e_i    
    
def test():
    L = longest_subpalindrome_slice
    print L('racecar')
    assert L('racecar') == (0, 6)
    assert L('Racecar') == (0, 6)
    assert L('RacecarX') == (0, 6)
    assert L('Race carr') == (6, 9)
    assert L('') == (0, 0)
    

print test()
