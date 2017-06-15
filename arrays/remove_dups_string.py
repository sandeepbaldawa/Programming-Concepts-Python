'''
Given a string that contains duplicate occurrences of characters, remove these duplicate occurrences.

For example, if the input string is "abbabcddbabcdeedebc", after removing duplicates it should become "abcde".

Time O(N)
Space O(N)
'''

def remove_duplicates(input):
    if len(input) <= 1:
        return input
    read_idx, write_idx = 0 , 0
    hashset = set()
    for each in input:
        if each not in hashset:
            hashset.add(each)
            input[write_idx] = input[read_idx]
            write_idx += 1
        read_idx += 1

    for idx in range(write_idx,len(input)):
        del input[-1]
    return input


input = [each for each in "abbabcddbabcdeedebc"]
print remove_duplicates(input)
