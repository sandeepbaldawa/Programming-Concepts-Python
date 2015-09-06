#!/usr/bin/python
# -*- coding: utf-8 -*-


class Node:

    def __init__(self, data=None):
        self.next = None
        self.data = data


class Queue:

    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        tmp = Node(data)
        tmp.next = None

        if self.tail:
            self.tail.next = tmp

        self.tail = tmp

        if not self.head:
            self.head = self.tail

    def dequeue(self):
        if not self.head:
            return head

        if not self.head.next:
            tail = None
            tmp = self.head
            self.head = self.head.next
        return tmp.data


myqueue = Queue()
myqueue.enqueue(10)
print myqueue.dequeue()
myqueue.enqueue(20)
print myqueue.dequeue()
