# https://youtu.be/nO7_qu2kd1Q
"""
Implement pow(A, B) % C.

In other words, given A, B and C, 
find (AB)%C.

Input : A = 2, B = 3, C = 3
Return : 2 
2^3 % 3 = 8 % 3 = 2


X ^ N % M = ((X ^ N/2) % M * (X ^ N/2) % M) % M   ==> if N is even
X ^ N % M = (X % M * (X ^ N-1) % M) % M   ==> if N is odd
1 ==> N is 0
"""
