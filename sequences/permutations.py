def getPermutations(A, K=0):
    if K == len(A):
    	print A

    for i in xrange(K, len(A)):
        A[i], A[K] = A[K], A[i] # swap
        getPermutations(A, K+1)
        A[K], A[i] = A[i], A[K] # swap restore
        
if __name__ == "__main__":
    getPermutations([1,2,3])
