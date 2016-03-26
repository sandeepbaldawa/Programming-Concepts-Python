# Uses python3
'''
The goal of this problem is to represent a given positive
integer n as a sum of as many pairwise distinct positive integers
as possible.

FOR 7
1+2 < 7  s: 1
s+2+3 < 7 s: 1+2

s+3+4 > 7 AND s+3 != 7 so s: 1+2
s+4+5 > 7 BUT s+4 == 7 s0 s: 1+2+4

FOR 9
1+2 < 9  s: 1
s+2+3 < 9 s: 1+2

s+3+4 > 9 AND s+3 != 9 so s: 1+2
s+4+5 > 9 AND s+4 != 9 so s: 1+2
s+5+6 > 9 AND s+5 != 9 so s: 1+2

s+6+7 > 9 BUT s+6 == 9 so s: 1+2+6
'''

n = int(input())
result = []
sum = 0

for i in range(1,int(n/2+1)):
        #sum + i + (i+1) <= n
        #if ((sum + i == n) or (sum + 1 + 2*i) <= n):
        if ((sum + 1 + 2*i) <= n):
                sum += i
                result.append(str(i))
        else:
                break

result.append(str(n-sum))
print(len(result))
print(" ".join(result))
~
