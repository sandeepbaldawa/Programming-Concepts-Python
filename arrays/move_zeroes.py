'''
Given an integer array, move all elements containing '0' to the left while maintaining the order
of other elements in the array. Let's look at the following integer array.
Input => 1 10 20 0 59 63 0 88 0

Ans =>   0 0 0 1 10 20 59 63 88

Algo:-
Init read_idx, write_idx = end of array
everytime read_idx equals non-zero arr[write_idx] = arr[read_idx] and write_idx-=1, for zero value skip
always read_idx -= 1

Time:- O(N)
Space:- O(1)
'''
def move_zeroes(arr):
    if not arr:
        return arr
    read_idx = write_idx = len(arr) - 1 #last element
    while(read_idx >= 0):
        if arr[read_idx] != 0:
            arr[write_idx] = arr[read_idx]
            write_idx -=1
        read_idx -= 1
    for i in range(read_idx+1, write_idx+1):
        arr[i] = 0
    return arr

assert move_zeroes([1, 10, 20, 0, 59, 63, 0, 88, 0]) == [0, 0, 0, 1, 10, 20, 59, 63, 88]
assert move_zeroes([1, 10, 0]) == [0, 1, 10]
assert move_zeroes([0, 0, 0]) == [0, 0, 0]
assert move_zeroes([1, 2, 3]) == [1, 2, 3]
assert move_zeroes([0]) == [0]
assert move_zeroes([1]) == [1]
assert move_zeroes([]) == []
