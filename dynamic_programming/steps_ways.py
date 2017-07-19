'''
Davis has  staircases in his house and he likes to climb each staircase 1,2  or 3 steps at a time. 
Being a very precocious child, he wonders how many ways there are to reach the top of the staircase.

Given the respective heights for each of the  staircases in his house, find and print the 
number of ways he can climb each staircase on a new line.


'''

def number_ways(n):
    table=[]
    #insert base case
    table.insert(0,1);
    table.insert(1,1);
    table.insert(2,2); #(1,1|2) 2 ways 
    table.insert(3,4); #(1,2| 1,1,1|2,1|3) 4 ways 
    #Iterate if N >= 4
    for i in range(4,n+1):
        val = table[i-1] + table[i-2] +table[i-3]
        table.insert(i,val);
    return table[n]

s = int(raw_input().strip())
for a0 in xrange(s):
    n = int(raw_input().strip())
    print number_ways(n)
    

    
