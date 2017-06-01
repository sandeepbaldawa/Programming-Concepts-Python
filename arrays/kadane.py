'''
Kadane's algo says maximum sub of a subarray(contiguous)
in a given array

curr_max = max(curr_val_in arr, curr_max + curr_val_in arr)

0 1 2 3 4 5 6 7

'''

def Kadane(arr):
   max_curr = arr[0]
   max_global = arr[0]
   for idx in range(1, len(arr)):
      max_curr = max(arr[idx], max_curr + arr[idx])
      max_global = max(max_curr, max_global)
   return max_global


arr = [-2, -3, 4, -1, -2, 1, 5, -3]
print arr
print Kadane(arr)
