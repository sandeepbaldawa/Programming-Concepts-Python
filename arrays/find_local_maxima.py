'''
Given an array of size n, find a peak element in the array. Peak element is the element which is greater than or equal to its neighbors.
For example - In Array {1,4,3,6,7,5}, 4 and 7 are peak elements. We need to return any one peak element.

- Unique elements
- anyone peak element

Test Case:-
- len(arr) <=0 or arr is null

[15, 26, 25, 46, 45, 50, 60]

Algo:-
- Linear search O(N)
Can we do better?
Binary Search O(logN)
Input is ***not sorted
'''
def getLocalMaxima(arr):
    if len(arr) <=0 or not arr:
        return None

    start, end = 0 , len(arr) - 1
    n = len(arr)
    # Try search for maxima using BS
    while(start <= end):
        mid = start + (end - start)/2
        
        if ((mid == 0 and arr[mid] > arr[mid+1]) or (mid == n-1 and arr[mid] > arr[mid-1]) or (arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1])):
            return arr[mid]
        elif arr[mid-1] > arr[mid]:
            end = mid - 1
        elif arr[mid+1] > arr[mid]:
            start = mid + 1

arr = [60, 20, 48, 46, 45, 30, 25]
print getLocalMaxima(arr)
