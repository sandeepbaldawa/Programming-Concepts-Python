'''
Problem Statement
=================
This problem is about implementing an algorithm for the knapsack without repetitions problem.
Also called as 0/1 Knapsack. Given weights(w) and value of items(w), the goal is to maximize
the value, keeping in mind the maximum value possible i.e. the Knapsack size(W)

Runtime Analysis
----------------
Time complexity - O(W*total items)

References
----------
https://www.youtube.com/watch?v=8LusJS5-AGo
'''

# Uses python3
import sys

def optimal_weight(W, w):
    
    rows = len(w) + 1
    cols = W + 1
    
    K = [[0 for _ in range(cols)] for _ in range(rows)]
    
    # Build table K[][] in bottom up manner
    for i in range(1,rows):
        for j in range(1,cols):
        	if j < w[i-1]:
        		K[i][j] = K[i-1][j]
        	else:
        		K[i][j] = max(w[i-1] + K[i-1][j-w[i-1]], K[i-1][j])
    
    return K[i][j]
    
__name__ = '__main__'
if __name__ == '__main__':
    #input = sys.stdin.read()
    input = "10 3 1 4 8"
    W, n, *w = list(map(int, input.split()))
    expected = 9
    assert expected == optimal_weight(W, w)
