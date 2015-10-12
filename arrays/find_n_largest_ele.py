One could sort and then find element that would be O(N logN)
Below can be done in O(N)
Worst case if you always choose the smallest element as the pivot O(N^2)

RSelect(A, n, order statistic i)
0 - If n == 1 return A[1]
1 - Choose pivot from A uniformly random
2 - Partition around the pivot with j being the new index of the partition
3 - If j == i return pivot  (dumb luck the pivot was our ith order statistic)
4 - If j > i  RSelect(A, j-1, i) => 1st part
5-  If i > j  RSelect(A, n-j, i-j) => 1st part


Choose a good pivot
-------------------
Median of Medians
ChoosePivot(A,n)
1 - break A into n/5 groups with 5 elements each
2 - Sort each group (mergesort)
3 - Copy n/5 medians(middle element of each sorted group) into new array C
4 - 

