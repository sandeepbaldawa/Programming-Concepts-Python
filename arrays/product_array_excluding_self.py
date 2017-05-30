'''

Given an array of integers arr, you’re asked to calculate for each index i the product of all integers 
except the integer at that index (i.e. except arr[i]). Implement a function arrayOfArrayProducts that 
takes an array of integers and returns an array of the products.

Solve without using division and analyze your solution’s time and space complexities.

Examples:

input:  arr = [8, 10, 2]
output: [20, 16, 80] # by calculating: [10*2, 8*2, 8*10]

input:  arr = [2, 7, 3, 4]
output: [84, 24, 56, 42] # by calculating: [7*3*4, 2*3*4, 2*7*4, 2*7*3]
'''

'''
O(N^2)
'''
def arrayOfArrayProducts(arr):
  if len(arr) <= 1:
    return []
  res = []
  # Loop through all ele
  for i in range(len(arr)):
    prod = 1
    # Calculate prod for each index
    for j in range(len(arr)):
      if i != j:
        prod = prod * arr[j]
    res.append(prod)
  return res

'''
O(N)
'''
def arrayOfArrayProducts1(arr):
  if len(arr) <= 1:
    return []
  res_prod = [0] * len(arr)
  prod = 1

  # Product of all nos from left of an num
  # for index == 0 product would be 1
  for idx, val in enumerate(arr):
    res_prod[idx] = prod
    prod = prod * val

  # Product of all nos from right of an num
  # for index == len(arr) -1 product would be 1
  prod = 1
  for idx in range(len(arr)-1, -1, -1):
    res_prod[idx] *= prod
    prod = prod * arr[idx]

  return res_prod


arr = [8, 10, 2]
arr1 = [2, 7, 3, 4]
print arrayOfArrayProducts1(arr1)
