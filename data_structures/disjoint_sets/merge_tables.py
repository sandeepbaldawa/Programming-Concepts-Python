'''
Problem Introduction
In this problem, your goal is to simulate a sequence of merge operations with tables in a database.
Problem Description
Task. There are n tables stored in some database. The tables are numbered from 1 to n. All tables share
the same set of columns. Each table contains either several rows with real data or a symbolic link to
another table. Initially, all tables contain data, and i-th table has ri rows

Sample 1.
Input:
5 5
1 1 1 1 1
3 5
2 4
1 4
5 4
5 3
Output:
2
2
3
5
5
Explanation:
In this sample, all the tables initially have exactly 1 row of data. Consider the merging operations:
1. All the data from the table 5 is copied to table number 3. Table 5 now contains only a symbolic
link to table 3, while table 3 has 2 rows. 2 becomes the new maximum size.
2. 2 and 4 are merged in the same way as 3 and 5.
3. We are trying to merge 1 and 4, but 4 has a symbolic link pointing to 2, so we actually copy
all the data from the table number 2 to the table number 1, clear the table number 2 and put a
symbolic link to the table number 1 in it. Table 1 now has 3 rows of data, and 3 becomes the
new maximum size.
4. Traversing the path of symbolic links from 4 we have 4 → 2 → 1, and the path from 5 is 5 → 3.
So we are actually merging tables 3 and 1. We copy all the rows from the table number 1 into
the table number 3, and now the table number 3 has 5 rows of data, which is the new maximum.
5. All tables now directly or indirectly point to table 3, so all other merges won’t change anything.


'''


#!/usr/bin/python
# -*- coding: utf-8 -*-
# python3

import sys

(n, m) = map(int, sys.stdin.readline().split())

# n,m = 5,5,

lines = list(map(int, sys.stdin.readline().split()))

# lines = [1,1,1,1,1]

rank = [0] * n
parent = list(range(0, n))
ans = max(lines)


def getParent(table):

    # print(table,parent[table])

    if table != parent[table]:
        parent[table] = getParent(parent[table])
    return parent[table]


def merge(destination, source):
    global ans

    # print(destination,source)

    (realDestination, realSource) = (getParent(destination),
            getParent(source))
    if realDestination == realSource:
        return
    if rank[realSource] > rank[realDestination]:
        parent[realDestination] = realSource
        lines[realSource] = lines[realDestination] + lines[realSource]
        if lines[realSource] > ans:
            ans = lines[realSource]
    else:
        parent[realSource] = realDestination
        lines[realDestination] = lines[realDestination] \
            + lines[realSource]
        if lines[realDestination] > ans:
            ans = lines[realDestination]
        if rank[realSource] == rank[realDestination]:
            rank[realDestination] = rank[realDestination] + 1
    return


# d = [3,2,1,5,5]
# s = [5,4,4,4,3]

for i in range(m):

    # destination, source = map(int, sys.stdin.readline().split())
    # destination, source = map(int, [d[i],s[i]])
    # merge(d[i]-1, s[i]-1)

    (destination, source) = map(int, sys.stdin.readline().split())
    merge(destination - 1, source - 1)

    # ans = max(lines)

    print ans

			
