def isSumMatch(a):
    left_idx = 0
    right_idx = len(a) - 1
    sum_left = a[left_idx]
    sum_right = a[right_idx]
    while (left_idx != right_idx):
        #print sum_left, sum_right
        if  (sum_left < sum_right):
            left_idx += 1
            sum_left += a[left_idx]
        else:    
            right_idx -= 1
            sum_right += a[right_idx]
    return sum_left == sum_right       
             
            

if __name__ == "__main__":
    num_tests = int(raw_input())
    #print num_tests
    for _ in range(num_tests):
        n = int(raw_input())
        input = map(int, raw_input().split(" "))
        if isSumMatch(input):
            print "YES"
        else:
            print "NO"
