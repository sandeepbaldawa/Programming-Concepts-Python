# A => 1
# B => 2
# C => 3
# D => 4
# E => 5
# F => 6
# G => 7
# H => 8
# AA => 27
# BA => 53


import time
def getExcelConversion(s):
	res = 0
	start = time.time()
	for i in range(0,len(s)):
		res = res * 26 + ord(s[i]) - ord('A') + 1
	end = time.time()	
	print str(end - start)	
	return res

def getExcelConversion_unoptimized(s):
	res = 0
	start = time.time()
	for i in range(0,len(s)):
		res = res + ((ord(s[i]) - ord('A') + 1) * 26**(len(s)-i-1))
	end = time.time()	
	print str(end - start)	
	return res

print getExcelConversion("ZZZZZZZZZZZZ")	
print getExcelConversion_unoptimized("ZZZZZZZZZZZZ")		
