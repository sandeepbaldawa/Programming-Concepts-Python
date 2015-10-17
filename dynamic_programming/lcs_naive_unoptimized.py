# A Naive recursive implementation of LCS problem

def lcs_helper(X, Y, m, n):
   if (m == 0 or n == 0):
     return 0
   if (X[m-1] == Y[n-1]):
     return 1 + lcs_helper(X, Y, m-1, n-1);
   else:
     return max(lcs_helper(X, Y, m, n-1), lcs_helper(X, Y, m-1, n))

def lcs(X, Y):
    return lcs_helper(X, Y, len(X), len(Y))
print lcs("MAN","CHIMPANZEE")
