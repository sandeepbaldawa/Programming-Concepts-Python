def getSubsets(A):
    if len(A) <= 1:
    	return [A, []]

    cache = getSubsets(A[:-1])
    return cache + [ s + [A[-1]] for s in cache]
        

if __name__ == "__main__":
    print getSubsets([1,2,3])
