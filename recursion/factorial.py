def Factorial(N):
	if N == 1:
		return 1
	return N * Factorial(N-1)
	
print Factorial(4)
print Factorial(3)
print Factorial(2)
print Factorial(1)
