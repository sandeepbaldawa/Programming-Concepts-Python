#!/usr/bin/python
# -*- coding: utf-8 -*-
# Uses python3

'''
Problem Statement
=================
Given two strings s and t, find the minimum number of edits 
(edit one character to another delete char from str1
or delete char from str2) to change str1 to str2.

Runtime Analysis
----------------
Time complexity - O(len(s) * len(t))
'''

def edit_distance(s, t):
    rows = len(t) + 1
    cols = len(s) + 1

    T = [[0 for _ in range(cols)] for _ in range(rows)]

    for j in range(cols):
        T[0][j] = j

    for i in range(rows):
        T[i][0] = i

    for i in range(1, rows):
        for j in range(1, cols):
            if s[j - 1] == t[i - 1]:
                T[i][j] = T[i - 1][j - 1]
            else:
                T[i][j] = 1 + min(T[i - 1][j], T[i][j - 1], T[i - 1][j- 1])

    return T[rows - 1][cols - 1]


__name__ = '__main__'
if __name__ == '__main__':
    str1 = 'ab'
    str2 = 'b'
    expected = 1
    assert expected == edit_distance(str1, str2)

    str1 = 'short'
    str2 = 'ports'
    expected = 3
    assert expected == edit_distance(str1, str2)

    str1 = 'a'
    str2 = 'a'
    expected = 0
    assert expected == edit_distance(str1, str2)
