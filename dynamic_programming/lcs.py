# https://www.youtube.com/watch?v=ml0i13Uvmuc
# Longest common subsequence
# Input   :- A[1..M],B[1..N] Output  :- C[1..P]
# Subsequence of A and B
# X is a subsequence of Y if X is obtained by dropping elements of Y
# "ad" is a subsequence of "abcde"
# A="abcde" and B="bceadq"  => "bcd" and "ad" are common sequences
# LCS of A and B is "bcd" and "bce"

# LCS represent similarity of A and B, longer the subsequence is more similar A and B are.
# Used to compare DNA sequences to know similarity between genes
# Mis-spelt word

# Brute Force
# 1. Generate all subsequences of A   (2^M)
# 2. generate all subsequences of B   (2^N) 
# 3. Retain the longest               O(2^Max(M.N))

# Recursive procedure
# Search(S){
#     Divide in to SubSpaces S1,S2,S3..Sk
#     Find the best in each Si
#     Find the best of the best
#}

# Techniques:- Optimal sub-structure and Overlapping sub-problem

#Psuedo Code
# for all in i : LCS(i,0) = 0
# for all in j : LCS(0,j) = 0
# if X[i] == X[j] : 1 + LCS(i-1, j-1)
# if X[i] != X[j] : max(LCS(i-1,j), LCS(i,j-1))

# X="ABA" and Y="ACBA"
# since X[3] == X[4]: LCS(3,4) =  1 + LCS(2,3)
# since X[2] == X[3]: LCS(2,3) =  1 + LCS(1,2)
# since X[1] = X[2] : LCS(1,2) = max(LCS(0,2), LCS(1,1))
# Since X[1] = Y[1] : LCS[0,2] = 0 and LCS[1,1] = 1 + LCS[0,0]
# Hence :  LCS[1,2] = 1
#          LCS[2,3] = 2
#          LCS[3,4] = 3

     
