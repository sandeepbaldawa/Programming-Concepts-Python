'''
Given a list of array, return a list of arrays, each array is a combination of one element in each given array.
Let me give you an example to help you understand the question Suppose the input is [[1, 2, 3], [4], [5, 6]], 
the output should be [[1, 4, 5], [1, 4, 6], [2, 4, 5], [2, 4, 6], [3, 4, 5], [3, 4, 6]].
'''

def perm_list(input, i=0, acc=""):
    '''
    input is [[1, 2, 3], [4], [5, 6]], the output should be
    [[1, 4, 5], [1, 4, 6], [2, 4, 5], [2, 4, 6], [3, 4, 5], [3, 4, 6]].

    :return: list of arrays
    '''
    if acc and len(acc) >= len(input):
        res.append(list(acc))
        return

    for idx, val in enumerate(input[i]):
        perm_list(input, i+1, acc + str(val))

res = []
input = [[1, 2, 3], [4], [5, 6]]
perm_list(input)
assert res == [['1', '4', '5'], ['1', '4', '6'], ['2', '4', '5'], ['2', '4', '6'], ['3', '4', '5'], ['3', '4', '6']]

res = []
input = [[]]
perm_list(input)
assert res == []
