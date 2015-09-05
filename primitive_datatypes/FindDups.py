#!/usr/bin/python
# -*- coding: utf-8 -*-


def findDups(A):
    for i in xrange(0, len(A)):
        curr = i
        while True:
            next = A[curr]
            tmp = A[next]
            if next == i:
                break
            if next == curr:
                print ' Found Dup %s' % next
                return next
            A[next] = A[curr]
            curr = tmp


A = [1, 2, 3, 4, 4]
findDups(A)

			
