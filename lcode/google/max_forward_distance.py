'''
Given an array find the maximum difference between any two numbers in the forward direction
'''

#[7, 9, 5, 6, 3, 2 ]
# each num
# Running min
# number minus minimum
import sys

def forward_diff(input):
  max_diff, minsoFar = -sys.maxint, input[0]
  for idx in range(1, len(input)):
    if input[idx-1] < minsoFar:
      minsoFar = input[idx-1]
    max_diff = max((input[idx] - minsoFar), max_diff)
  return max_diff
  
input = [7, 9, 5, 6, 3, 2 ]
print forward_diff(input)
