'''
Count number of Island's i.e.
number of adjacent 1's in a given matrix.

Clarification:-
Dont take diagonal take only 1's which are adhacent by row or col

Tests:-
Empty arry or size of array is "0" return 0
1's and 0's combinations
All 1's

Algo:-
Run DFS on all the nodes which have 1 and not marked visited.
Anytime we explore 1 we mark it visited.
Increment count only when we encounter the first 1 in an island.

'''
def findIslandCount(arr):
    if not arr or len(arr) <= 0:
        return 0

    return helper(arr, len(arr), len(arr[0]))

def helper(arr, m, n):
    count = 0
    for row in range(m):
        for col in range(n):
            if arr[row][col] == 1 and not visited[row][col]:
                count += 1
                explore(arr, row, col, m , n)

    return count

def explore(arr, row, col, m , n):
    '''
    Run DFS here for each row and column index to find all
    neighbouring 1's
    :param arr:
    :param row:
    :param col:
    :return:
    '''
    # explore if 1 and not visited
    if row >= 0  and row < m and col >= 0 and col < n and arr[row][col] == 1 and not visited[row][col]:
        visited[row][col] = True
        explore(arr, row - 1, col, m , n)
        explore(arr, row + 1, col, m, n)
        explore(arr, row, col - 1, m, n)
        explore(arr, row, col + 1, m, n)
    return

arr = [[1, 1, 1, 1],
       [1, 1, 1, 1],
       [1, 1, 1, 0],
       [1, 1, 1, 1]]
visited = [[False]* (len(arr)+1) for _ in range(len(arr[0])+1)]
print findIslandCount(arr)
