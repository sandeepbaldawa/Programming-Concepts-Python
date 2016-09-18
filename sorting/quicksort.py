QuickSort is a divide and conquer algo for sorting
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
Ranking algo
============
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
   In short we are sorting one element(pivot) in each iteration, so worst case will take O(N^2)
6. At the end swap(a[i+1], pivot)   
Partition algo
==============
Returns the point at which partition is done based on the pivot element

---------------------------------------
| p |  |  |  |  | q |  |  |  |  |  |r |
---------------------------------------
q => partition
p => start
q => end

QuickSort algo
==============
QS(A, p, r):
  if p < r:
     q = partition(A, p, r)
     QS(A, p, q-1)
     QS(A,q+1, r)
     
How does it differ from mergsort?
=================================
Mergesort gives the midpoint whereas quicksort returns in the partition function the current pivot elements index which
may or may not be the midpoint. Chooding pivot is the key to make quicksort time complexity O(N*lgN) and space O(lgN)
     
Best case and worst case?
========================
Best case the elements are equally divided on left and right of pivot
QS(A, p, r):
  if p < r:
     q = partition(A, p, r) <== O(n)
     QS(A, p, q-1)          <== T(N/2) 
     QS(A,q+1, r)           <== T(N/2) 

T(n) = 2 * T(n) + O(n) 

Worst case the elements are divided one element on the left and n-1 elements on right of pivot
QS(A, p, r):
  if p < r:
     q = partition(A, p, r) <== O(n)
     QS(A, p, q-1)          <== T(1) 
     QS(A,q+1, r)           <== T(n-1) 

T(n) = T(1) + T(n-1) + C*O(n)
     = T(n-2) + C*O(n-1) + C*O(n)
     = T(n-3) + C*O(n-2) + C*O(n-1) + C*O(n)
     = C + 2*C + 3*C + 4*C..n*C
     = O(N^2)

When will worst case O(N^2) happen in quicksort?
================================================
When input is already sorted (divide is T(1) and T(n-1))

What will be complexity of Quicksort if median is taken as the pivot?
=====================================================================
Here divide is T(n/2) and T(n/2)
O(N*logN)

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
