One could sort and then find element that would be O(N logN)
Below can be done in O(N)

RSelect(A, n, order statistic i)
0 - If n == 1 return A[1]
1 - Choose pivot from A uniformly random
2 - Partition around the pivot with j being the new index of the partition
3 - If j == i return pivot  (dumb luck the pivot was our ith order statistic)
4 - If j > i  RSelect(A, j-1, i) => 1st part
5-  If i > j  RSelect(A, n-j, i-j) => 1st part

