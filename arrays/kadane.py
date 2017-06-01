'''
Kadane's algo says maximum sub of a subarray(contiguous)
in a given array
'''

def Kadane(arr):
   max_curr=max_global=arr[0]
   for idx, val in enumerate(arr):
      max_curr = max(max_curr, max_curr + val)
      if max_curr > max_global:
         max_global = max_curr
    return max_global     
