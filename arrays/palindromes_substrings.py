'''
Find count of all palindromes in substrings
'''
def isPalindrome(input, i , j):
   tmp = input[i:j+1]
   #print tmp
   return tmp ==  tmp[::-1]


def getPalindromes(input):
   count = 0
   for i in range(len(input)):
      for j in range(len(input)):
         if isPalindrome(input, i , j):
            count += 1

   return count


def getPalindromesOptimized(input):
   count = 0
   for i in range(len(input)):
      for j in range(len(input)):
         if (i-j) < 0 or ((i+j) == len(input)):
           break
         if input[i+j] != input[i - j]:
            break
         else:
            count += 1

   for i in range(len(input)):
      for j in range(len(input)):
         if (i-j) < 0 or ((i+j+1) == len(input)):
           break
         if input[i+j+1] != input[i - j]:
            break
         else:
            count += 1

   return count

print getPalindromes("aabb")
print getPalindromesOptimized("bbaabb")
~                                       
