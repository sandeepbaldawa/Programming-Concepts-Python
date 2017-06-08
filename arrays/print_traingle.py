# write a function which takes one integer parameter,
# and print in such fashion:
# 1
# 2 3
# 4 5 6
# ... n, where n is the input parameter

#n => 0..
def printPattern(n):
    if n <= 0:
        print "0"
        return
    line_size, num  = 1, 1
    while(True):
        string = ""
        # print how many numbers on each line
        for i in range(line_size):
            if num >= n:
                string = string + str(num)
                return
            string = string + str(num) + " "
            num += 1
        line_size += 1

        
            
#printPattern(7)
#printPattern(0)
#printPattern(7)
#printPattern(106)
#printPattern(3)
