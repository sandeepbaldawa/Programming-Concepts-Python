# Count Number of inversions
'''
eg:-
Input:
5
2 3 9 2 9
Output:
2
'''
# Uses python3
import sys

def merge_count(A, B):
	global inversions
	C = []
	lenA, lenB = len(A), len(B)
	i, j = 0,0
	while(i < lenA and j < lenB):
		if A[i] <= B[j]:
			C.append(A[i])
			i+=1
		else:
			C.append(B[j])
			j+=1
			inversions = inversions + lenA - i
	if i == lenA:
		C.extend(B[j:])
	else:
		C.extend(A[i:])
	
	return 	C
	
def get_number_of_inversions(a, start, end):
	if (end - start) > 0:
		mid = start + (end-start)//2
		left  = get_number_of_inversions(a , start, mid)
		right = get_number_of_inversions(a, mid+1, end)
		return merge_count(left,right)
	else:	
		return a[start:end+1]

#input = sys.stdin.read()
input = "5 2 3 9 2 9"
n, *a = list(map(int, input.split()))
inversions = 0
get_number_of_inversions(a, 0 , len(a)-1)
print(inversions)
