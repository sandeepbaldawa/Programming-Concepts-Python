d = { '1': "1",
      '2': "ABC",
      '3': "DEF",
      '4': "GHI",
      '5': "JKL",
      '6': "MNO",
      '7': "PQRS",
      '8': "TUV",
      '9': "WXYZ",
}

def getphoneMneumonicHelper(input, digitIndex, acc):
	if digitIndex < len(input):
		digit = input[digitIndex]
		for c in d[str(ord(input[digitIndex]) - ord('0'))]:
			acc[digitIndex] =  c
			getphoneMneumonicHelper(input, digitIndex + 1, acc)
	else:
		print acc
	
acc = [None] * 3
getphoneMneumonicHelper("567", 0 , acc)
