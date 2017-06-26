'''
In American football what are the total possible drives of 2, 3 and 7
such that total might b equal to a specific score eg:- 5
For 5 we could have
2,3 or 3,2

Recursive Formula - CountComb(score_remain - 2) + CountComb(score_remain - 3) + CountComb(score_remain - 7)
Time:- O(3^N) # Eaach level worst case we branch thrice, assuming tree is not balanced worst case we branch for N/2 times
Space:- O(N), #Worst case if we take just 2 we get the longest height of the tree i.e. N/2

This is not an acceptable complexity due to the exponential nature of the solution, can we do better?
'''
scores = [2, 3, 7]
def CountComb(score_remain):
    if score_remain < 0:
        return 0
    
    # Target reached 
    if score_remain == 0:
        return 1

    c = 0
    for score in scores:
        c += CountComb(score_remain - score)
    return c

print CountComb(5)
