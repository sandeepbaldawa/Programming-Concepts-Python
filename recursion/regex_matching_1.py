'''

Implement a regular expression function isMatch that supports the '.' and '*' symbols. 
The function receives two strings - text and pattern - and should return true if the text 
matches the pattern as a regular expression. For simplicity, assume that the actual symbols '.'
and '*' do not appear in the text string and are used as special symbols only in the pattern string.

Logic
=====
1. Pattern and Text match and reach end of size
2. Text reaches end of size but pattern does not
3. Pattern reaches end of size but text does not
4. Character match or "." followed by "*"
5. Pattern and Text match

'''

def isMatchHelper(text, pattern, textIndex, patIndex):
   # Both text and pattern are of same length
   if (textIndex >= len(text) and patIndex >= len(pattern)):
      return True

   # text ended but pattern did not
   if textIndex >= len(text) and patIndex < len(pattern):
      if (pattern[patIndex+1] == '*'):
         return isMatchHelper(text, pattern, textIndex, patIndex + 2)
      else:
         return False

   # pattern ended but text did not
   if patIndex >= len(pattern) and textIndex < len(text):
      return False

   # string matching for character followed by '*'
   if (patIndex+1 < len(pattern) and pattern[patIndex+1] == '*'):
        if (pattern[patIndex] == '.') or (text[textIndex] == pattern[patIndex]):
            return (isMatchHelper(text, pattern, textIndex, patIndex + 2) or
                    isMatchHelper(text, pattern, textIndex + 1, patIndex))
        else:
            return isMatchHelper(text, pattern, textIndex, patIndex + 2)

   # match . or each character
   if (pattern[patIndex] == '.') or (pattern[patIndex] == text[textIndex]):
        return  isMatchHelper(text, pattern, textIndex + 1, patIndex + 1)
   return false

pat = "ab*c."
text = "acd"
print isMatchHelper(text, pat, 0 , 0)
