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

def match_regex(s, p):
  T = [[False] * (len(p)+1) for _ in range(len(s)+1)]
  T[0][0] = True
  
  for i in xrange(1, len(T[0])):
    if p[i-1] == "*":
      T[0][i] = T[0][i-2]
      
  for i in xrange(1, len(T)):
    for j in xrange(1, len(T[0])):
      if p[j-1] == "." or s[i-1] == p[j-1]:
        T[i][j] = T[i-1][j-1]
      elif p[j-1] == "*":
        T[i][j] = T[i][j-2] # * consume zero characters
        if s[i-1] == p[j-2] or p[j-2] == ".": # * consumes one or more
          T[i][j] = T[i-1][j]
      else:
        T[i][j] = False
        
  return T[len(s)][len(p)]
  
assert match_regex("aaa","aa") == False
assert match_regex("aaa","aaa") == True
assert match_regex("ab","a.") == True
assert match_regex("abbb","ab*") == True
assert match_regex("a","ab*") == True
assert match_regex("abbc","ab*") == False
        
        
