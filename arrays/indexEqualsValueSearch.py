'''

Array Index & Element Equality

Given a sorted array arr of distinct integers, write a function indexEqualsValueSearch that returns an index i for which arr[i] == i. Return -1 if there is no such index. Analyze the time and space complexities of your solution and explain its correctness.

Examples:

input: arr = [-8,0,2,5]
output: 2 # since arr[2] == 2

input: arr = [-1,0,3,6]
output: -1 # since no index in arr satisfies arr[i] == i.
Constraints:

[time limit] 5000ms

[input] array.integer arr

1 ≤ arr.length ≤ 100
[output] integer
'''

def indexEqualsValueSearch(arr):
   start, end = 0, len(arr)

   while(start <= end):
      mid = start + (end - start)/2
      if arr[mid] == mid:
         return mid
      elif arr[mid] < mid:
         start = mid + 1
      else:
         end = mid - 1
   return -1

arr = [-8,0,2,5]
arr = [-8,0,3,5]
arr = [0,300,301,302,303]
arr = [0]
arr = [-1]
print indexEqualsValueSearch(arr)
