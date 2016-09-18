QuickSort 
Worst => O(N^2)
Average => O(N logN)

How does it work ?
==================
Pick an element and place it such that all elements to the left of the element are less than or equal and the right element
are greater than the element. Fundamentally we are ranking the element(Kth largest element), essentially one element at a time.

Sorting is never needed for ranking an element.

Follows divide and conquer algorithm

When to use quicksort ?
======================
When number of elements are not so large the complexity is better than merge sort eg:- 100 elements.

Trick to understand algo?
===========================
For ranking use the below:-
1.Choose a pivot element
2.Take two indice i=0 & j=0
3. Keep traversing arry by incrementing j++
4. if a[j] <= pivot 
      increment i++
      swap(a[i], a[j])
      increment j++
   else
      increment j++
5. Keep continuing at the end of O(N) we will get rank of the pivot element.      


# Given a list, use the last element in the list as the pivot to partition the
# list into those less than or equal to the pivot, the pivot itself and those
# greater. Return the final index of the pivot. Assume that start and end are
# given the range of the list. Assume both are inclusive and the list is not
# empty.
def partition(li, start, end):
  if start == end:
    return start
  pivot = li[end]  # last element
  rightPartStartIndex = start
  for i in range(start, end):
    if (li[i] <= pivot):
      li[i], li[rightPartStartIndex] = li[rightPartStartIndex], li[i]
      rightPartStartIndex += 1
  li[end], li[rightPartStartIndex] = li[rightPartStartIndex], li[end]
  return rightPartStartIndex

def quickSort(li, start, end):
  pivot = partition(li, start, end)
  # If there is more than one element on the right
  # then quick sort the partition.
  if (pivot - start > 1):
    quickSort(li, start, pivot - 1)
  # If there is more than one element on the left
  # then quick sort the partition.
  if (end - pivot > 1):
    quickSort(li, pivot + 1, end)
