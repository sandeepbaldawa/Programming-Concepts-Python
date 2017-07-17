"""
Given a string, 
compute recursively (no loops) the number of "11" substrings in the string.
The "11" substrings should not overlap.
"""

def count11(str, count=0, idx=0):
  if idx >= (len(str)):
    print count
    return

  if str[idx:idx+2] == "11":
    count += 1
  elif str[idx:idx+1] == "1" or str[idx+1:idx+2] == "1":
    return count11(str, count, idx + 1)
  return count11(str, count, idx + 2)





count11("11abc11")
count11("abc11x11x11")
count11("111")
count11("1111")
count11("1")
count11("")
count11("hi")
count11("11x111x1111")
count11("1x111")
count11("1Hello1")
count11("Hello")
~                  
