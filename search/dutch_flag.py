def getPartition(A):
	"""
	In Place seperation of three items
	eg:- R,G and B 
	"""
	b1 = 0 #pointer to starting of bucket1
	b2 = 0 #pointer to starting of bucket2
	b3 = len(A) - 1 #pointer to starting of bucket3
	pivot = A[0] # choose any random element
	while b2 <= b3:
		print b1, b2, b3, pivot
		if A[b2] < pivot: # Add item to bucket1
			A[b1], A[b2] = A[b2], A[b1]
			b1 += 1
			b2 += 1
		elif A[b2] == pivot: # Add item to bucket2
			b2 += 1
		else:
			A[b2],A[b3] = A[b3],A[b2]
			b3 -= 1

A = [1, 0, 2, 0, 1, 2, 0, 1]
print A
getPartition(A)
print A
