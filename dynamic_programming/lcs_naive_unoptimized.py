"""
Problem Statement
=================
Given two sequences A = [A1, A2, A3,..., An] and B = [B1, B2, B3,..., Bm], find the length of the longest common
subsequence.

A Naive recursive implementation of LCS problem
From call stack we can see lot of calls being recalculated
Can we avoid this?
O(2 ^N)
"""

def lcs_helper(X, Y, m, n):
   if (m == 0 or n == 0):
     return 0
   if (X[m-1] == Y[n-1]):
     return 1 + lcs_helper(X, Y, m-1, n-1);
   else:
     return max(lcs_helper(X, Y, m, n-1), lcs_helper(X, Y, m-1, n))

def lcs(X, Y):
    return lcs_helper(X, Y, len(X), len(Y))
print lcs("AXYT","AYZX")


                     lcs("AXYT", "AYZX")
                       /                 \
         lcs("AXY", "AYZX")            lcs("AXYT", "AYZ")
         /            \                  /               \
lcs("AX", "AYZX") lcs("AXY", "AYZ")   lcs("AXY", "AYZ") lcs("AXYT", "AY")
