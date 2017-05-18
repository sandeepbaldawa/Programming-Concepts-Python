'''
Find numbers common in arr1 and arr2 and return them
Case1:- M almost equal to N
Time Complexity O(M + N)
Space Complexity O(N)
'''

def findDuplicates(arr1, arr2):
   i, j = 0, 0
   res = []

   while(i < len(arr1) and j < len(arr2)):
      if arr1[i] < arr2[j]:
         i += 1
      elif arr1[i] == arr2[j]:
         res.append(arr1[i])
         i += 1
         j += 1
      else:
         j += 1
   return res


arr1 = [1, 2, 3, 5, 6, 7]
arr2 = [3, 6, 7, 8, 20]
#print findDuplicates(arr1, arr2)

'''
Case2:- M extremely large compared to N
Time Complexity O(M lg N)
Space Complexity O(N)
'''

def findDuplicates2(arr1, arr2):
   res = []
   for num in arr1:
      if binarySearch(arr2, num) != -1:
         res.append(num)
   return res

def binarySearch(arr, num):
   start , end = 0 , len(arr)-1
   while(start <= end):
      mid = start + (end - start)/2
      if num < arr[mid]:
         end = mid - 1
      elif num == arr[mid]:
         return mid
      else:
         start = mid + 1
   return -1


arr1 = [1, 2, 3, 5, 6, 7]
arr2 = [3, 6, 7, 8, 20]
print findDuplicates2(arr1, arr2)
