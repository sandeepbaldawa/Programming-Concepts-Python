'''
Pairs with Specific Difference

Given an array arr of distinct integers and a nonnegative integer k, write a function findPairsWithGivenDifference that returns an array of all pairs [x,y] in arr, such that x - y = k. If no such pairs exist, return an empty array.

In your solution, try to reduce the memory usage while maintaining time efficiency. Prove the correctness of your solution and analyze its time and space complexities.

Note: the order of the pairs in the output array doesn’t matter.

Examples:

input:  arr = [0, -1, -2, 2, 1], k = 1
output: [[0, -1], [-1, -2], [2, 1], [1, 0]]

input:  arr = [1, 7, 5, 3, 32, 17, 12], k = 17
output: []
'''
'''
Time :- O(N logN) with no extra space
'''
def findPairsWithGivenDifference(arr, K):
  ''' Return x - y = k
       or empty
  '''
  arr.sort()
  first, last = 0, 1
  res = []
  while(first < len(arr) and last < len(arr)):
    if first != last and arr[last] - arr[first] == K:
       pair = [arr[first], arr[last]]
       res.append(pair)
       last += 1
    elif arr[last] - arr[first] < K:
       last += 1
    elif arr[last] - arr[first] > K:
       first += 1
  return res

arr = [0, -1, -2, 2, 1]
k = 1
print findPairsWithGivenDifference(arr, k)
