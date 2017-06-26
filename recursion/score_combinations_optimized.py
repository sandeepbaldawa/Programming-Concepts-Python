'''
In American football what are the total possible drives of 2, 3 and 7
such that total might b equal to a specific score eg:- 5
For 5 we could have
2,3 or 3,2

Bottom Up DP approach
Time:- O(N^2) 
Space:- O(N),

Code is generic form of below...
if score >= 2:
    a += dp[idx - 2]
 if score >= 3:
    a += dp[idx - 3]
 if score >= 5:
    a += dp[idx - 5]
'''
scores = [2, 3, 7]
def CountComb(target):
    '''Count all combinations of drive scores which can reach a specific target'''
    dp = [0 for _ in range(target)]
    dp[0] = 1
    a = 0
    for cscore_idx, current_score in enumerate(range(target)):
        for step_idx, step in enumerate(scores):
            if current_score >= step:
                a += dp[cscore_idx - step]

    return a
print CountComb(5)
