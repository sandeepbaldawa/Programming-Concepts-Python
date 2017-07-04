'''
Find the first unique integer from a set of arrays  
'''

'''
Answer below is "4", it is the first unique element present
in the array
Time:- O(N)
space:- O(N)
'''
def first_unique(input):
   if len(input) <= 0:
     return -1
   dict = {1:[],2:[]}
   for idx, val in enumerate(input):
      if val in dict[1]:
        dict[2].append(val)
      else:
        dict[1].append(val)

   for idx, val in enumerate(input):
      if val in dict[1] and val not in dict[2]:
         return val

   return -1

arr = [2,2,3,4,1,2,3]
print first_unique(arr)
