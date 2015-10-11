import sys
from sys import maxint
def max_sum_conti(arr):
    min_index = -1
    max_index = -1
    curr_min_index = -1
    start_max_index = -1
    min = 0#sys.maxint
    max = 0#-sys.maxint - 1
    sum = 0
    for e in range(0,len(arr)):
        sum+=arr[e]
        if (sum < min):
            min = sum
            curr_min_index = e
        if ((sum - min) > max):
            max = sum - min
            min_index = curr_min_index
            max_index = e
    print (min_index+1),max_index
max_sum_conti([-6, -2, 3, 4, -7])
