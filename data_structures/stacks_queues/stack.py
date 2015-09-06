#!/usr/bin/python
# -*- coding: utf-8 -*-


class Node:

    def __init__(self, data=None):
        self.next = None
        self.data = data


class Stack:

    def __init__(self):
        self.head = None

    def push(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = None
        else:
            tmp = Node(data)
            tmp.next = self.head
            self.head = tmp

    def pop(self):
        if not self.head:
            print 'Cannot pop from empty stack'
            return None
        else:
            tmp = self.head
            self.head = tmp.next
            tmp.next = None
        return tmp.data

    def peek(self):
        if not self.head:
            return None
        else:
            return self.head.data


mystack = Stack()
mystack.push(10)
mystack.push(20)
mystack.push(30)
print mystack.pop()
print mystack.pop()
print mystack.pop()
print mystack.pop()
print mystack.peek()
