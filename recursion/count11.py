"""
Given a string, 
compute recursively (no loops) the number of "11" substrings in the string.
The "11" substrings should not overlap.
"""

def count11(str, count=0):
    if len(str) <= 1:
        print "Count is ",count
        return
    
    if str[0:2] == "11":
        count = count + 1
    elif str[1] and str[1] == "1":
        return count11(str[1:], count)

    return count11(str[2:], count)
    
count11("11abc11")	    
count11("abc11x11x11")    
count11("111") 	    
count11("1111") 	    
count11("1") 	    
count11("") 
count11("hi")    
count11("11x111x1111")	    
count11("1x111") 	    
count11("1Hello1") 	    
count11("Hello") 
