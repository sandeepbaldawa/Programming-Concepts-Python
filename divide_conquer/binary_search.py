# Uses python3
'''
In this problem, you will implement the binary search algorithm that allows searching very efficiently (even
huge) lists provided that the list is sorted.

Input:
5 1 5 8 12 13
5 8 1 23 1 11
Output:
2 0 -1 0 -1
'''
import sys
import math

def binary_search(a, x):

        low, high = 0, len(a)-1
        while low <= high:
                mid = (low + math.ceil((high - low)//2))
                if a[mid] == x:
                        return mid
                elif x < a[mid]:
                        high = mid -1
                else:
                        low = mid + 1
        return -1
    # write your code here

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


input = sys.stdin.read()
#input = "10 2 3 4 5 6 7 8 9 10 11 12 1 2 3 4 5 6 7 8 9 10 11 12"

data = list(map(int, input.split()))


n = data[0]
m = data[n + 1]
a = data[1 : n + 1]
#print(a)
#print(data[n + 2:])
#print(n)
#print(m)
for x in data[n + 2:]:
    # replace with the call to binary_search when implemented
    print(binary_search(a, x), end = ' ')
