# Uses python3
import sys

def get_majority_element(a, left, right):
	#print(left,right)
	if right-left <= 1:
		return a[left]
	
	mid = left + (right-left)//2 
	
	left_majority = get_majority_element(a, left,  mid-1)
	right_majority = get_majority_element(a, mid, right)
	#print(left_majority, right_majority)
	if left_majority == -1 and right_majority == -1:
		return -1
	if left_majority != -1:
		if (a.count(left_majority) > len(a)//2):
			return left_majority
	if right_majority != -1:
		if (a.count(right_majority) > len(a)//2):
			return left_majority
	if left_majority == right_majority:
		return left_majority
	return -1
  
__name__ = '__main__'
if __name__ == '__main__':
    #input = sys.stdin.read()
    #input = "10 512766168 717383758 5 126144732 5 573799007 5 5 5 405079772"
    #input = "10 2 124554847 2 941795895 2 3 2 2 792755190 756617003"
    #input = "5 2 3 9 2 2"
    input = "5 1 1 1 2 2"
    
    n, *a = list(map(int, input.split()))
    #print(n,a)
    if get_majority_element(a, 0, n-1) != -1:
        print(1)
    else:
        print(0)
