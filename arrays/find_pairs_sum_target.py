'''
Find pair of numbers whose sum matches a given target
'''

def find_pairs(input, target):
   match_dict = {}
   res = []
   for idx, val in enumerate(input):
      tmp = target - val
      if tmp in match_dict.keys():
         pair=(val, tmp)
         res.append(pair)
      match_dict[val] = True
   return res

input=[]
target=-2
print find_pairs(input, target)
