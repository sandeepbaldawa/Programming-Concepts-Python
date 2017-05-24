#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Given an unsorted array of integers arr and a number s, write a function findArrayQuadruplet that finds four numbers (quadruplet) in arr that sum
up to s. Your function should return an array of these numbers in an ascending order. If such a quadruplet doesn’t exist, return an empty array.
Note that there may be more than one quadruplet in arr whose sum is s. You’re asked to return the first one you encounter.
Explain and code the most efficient solution possible, and analyze its time and space complexities.
Example:
input:  arr = [2, 7, 4, 0, 9, 5, 1, 3], s = 20
output: [0, 4, 7, 9] # The ordered quadruplet of (7, 4, 0, 9)
                     # whose sum is 20. Notice that there
                     # are two other quadruplets whose sum is 20:
                     # (7, 9, 1, 3) and (2, 4, 9, 5), but again you’re
                     # asked to return the just one quadruplet (in an
                     # ascending order)
'''
# O(N^3)

def findArrayQuadruplet(arr, s):
    if len(arr) <= 3:
        return arr
    arr.sort()

  # Outer
    for (i, vali) in enumerate(arr):
     # Innner
        for (j, valj) in enumerate(arr):
        # Two pointer logic
            start = j + 1
            end = len(arr) - 1
            while start < end:
                if vali + valj + arr[start] + arr[end] > s:
                    end -= 1
                elif vali + valj + arr[start] + arr[end] < s:
                    start += 1
                else:
                    return [vali, valj, arr[start], arr[end]]

arr = [2, 7, 4, 0, 9, 5, 1, 3]
s = 20
print findArrayQuadruplet(arr, s)
