'''
Task. You are given a description of a rooted tree. Your task is to compute and output its height. Recall
that the height of a (rooted) tree is the maximum depth of a node, or the maximum distance from a
leaf to the root. You are given an arbitrary tree, not necessarily a binary tree.

Input:
5
4 -1 4 1 1
Output:
3

'''

#!/usr/bin/python
# -*- coding: utf-8 -*-
# python3

import sys
import threading
sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 25)  # new thread will get stack of such size


class TreeHeight:

    def read(self):
        self.n = 5  # int(sys.stdin.readline())
        self.parent = [4, -1, 4, 1, 1]  # list(map(int, sys.stdin.readline().split()))

    def get_depth(self, vertex):

            # if depth is already found nothing to do
            # print(vertex)

        if self.depth[vertex] != 0:
            return

        if self.parent[vertex] == -1:
            self.depth[vertex] = 1
            return

        if self.depth[self.parent[vertex]] == 0:
            self.get_depth(self.parent[vertex])

        self.depth[vertex] = self.depth[self.parent[vertex]] + 1
        return

    def compute_height(self):
        maxHeight = 0
        self.depth = [0 for each in range(self.n)]
        for vertex in range(self.n):
            self.get_depth(vertex)
            if self.depth[vertex] > maxHeight:
                maxHeight = self.depth[vertex]

            # print(self.depth)....

        return maxHeight


def main():
    tree = TreeHeight()
    tree.read()
    print tree.compute_height()
threading.Thread(target=main).start()
