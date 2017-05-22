'''
Given an array of unique characters arr and a string str, Implement a function getShortestUniqueSubstring that finds the smallest substring of str containing all the characters in arr. Return "" (empty string) if such a substring doesn’t exist.

Come up with an asymptotically optimal solution and analyze the time and space complexities.

Example:

input:  arr = ['x','y','z'], str = "xyyzyzyx"

output: "zyx"

'''

def reset_dict(dict):
   for k,v in dict.items():
      dict[k] = 0

def getShortestUniqueSubstring(arr, str):
   dict_arr = {}
   if len(arr) <= 0 or len(str) <=0:
       return []
   # Input each array element into dict
   for each in arr:
     dict_arr[each] = 0

   #matching index and match count
   i_m,  match_count = 0, 0
   res = []

   # search str for matches
   for idx in range(len(str)):
      i_m = idx
      
      # Check for matches
      while((str[i_m] in dict_arr.keys()) and (dict_arr[str[i_m]] == 0) and i_m < len(str)):
        res.append(str[i_m])
        dict_arr[str[i_m]] = 1
        i_m += 1
        match_count += 1
        if match_count == len(arr):
           return res
      #Reset if no match
      match_count = 0
      reset_dict(dict_arr)
      res = []



arr = ['x','y','z']
str = "xyyzyzyx"
assert(getShortestUniqueSubstring(arr, str) == ['z','y','x'])
arr = ['x','y','z']
str = "zyx"
assert(getShortestUniqueSubstring(arr, str) == ['z','y','x'])
arr = []
str = "xyz"
assert(getShortestUniqueSubstring(arr, str) == [])
arr = ['x']
str = "xyyzyzyx"
assert(getShortestUniqueSubstring(arr, str) == ['x'])
arr = ['a','b','c','d','e','f']
str = "xyyfdecbazyzyx"
assert(getShortestUniqueSubstring(arr, str) == ['f','d','e','c','b','a'])
