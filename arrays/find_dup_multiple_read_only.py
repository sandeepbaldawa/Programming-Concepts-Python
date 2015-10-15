# http://stackoverflow.com/questions/7117388/finding-out-the-duplicate-element-in-an-array

# "You are given an array of integers of length n, where each element ranges
#  from 0 to n - 2, inclusive.  Prove that at least one  duplicate element must
#  exist, and give an O(n)-time, O(1)-space algorithm for finding some
#  duplicated element.  You must not modify the array elements during this 
#  process."

# Solution:- http://keithschwarz.com/interesting/code/?dir=find-duplicate

def findArrayDuplicate(array):
    assert len(array) > 0

    # The "tortoise and hare" step.  We start at the end of the array and try
    # to find an intersection point in the cycle.
    slow = len(array) - 1
    fast = len(array) - 1

    # Keep advancing 'slow' by one step and 'fast' by two steps until they
    # meet inside the loop.
    while True:
        slow = array[slow]
        fast = array[array[fast]]

        if slow == fast:
            break

    # Start up another pointer from the end of the array and march it forward
    # until it hits the pointer inside the array.
    finder = len(array) - 1
    while True:
        slow   = array[slow]
        finder = array[finder]

        # If the two hit, the intersection index is the duplicate element.
        if slow == finder:
            return slow
