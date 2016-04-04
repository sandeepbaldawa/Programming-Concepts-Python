'''
You are given a primitive calculator that can perform the following three operations with the current number
x: multiply x by 2, multiply x by 3, or add 1 to x. Your goal is given a positive integer n, find the
minimum number of operations needed to obtain the number n starting from the number 1.

eg:-
Input:
5
Output:
3
1 2 4 5

Input:
96234
Output:
14
1 3 9 10 11 22 66 198 594 1782 5346 16038 16039 32078 96234
'''
# Uses python3
import sys

def optimal_sequence(n):
    s = [0] * (n+5)
    s[1] = 0
    s[2] = 1
    s[3] = 1
    for i in range(4,n+1):
        s[i] = min (1 + s[i-1], 1 + s[i//2] if i % 2 == 0 else 1000000, 1 + s[i//3] if i % 3 == 0 else 1000000)
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0 and (s[n] == s[n//3] + 1):
                n = n // 3
        elif n % 2 == 0 and (s[n] == s[n//2] + 1):
                n = n // 2
        else:
                n = n - 1

    return reversed(sequence)
input = sys.stdin.read()
#input = 96234
n = int(input)
sequence = list(optimal_sequence(n))
#print(sequence)
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
