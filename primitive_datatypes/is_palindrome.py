def is_palindrome(input):
	i , j = 0, len(input)-1
	print i,j

	while(i < j):
		while(i < j and not input[i].isalnum):
			i += 1
		while(i < j and not input[j].isalnum):
			j -= 1
		
		if input[i].lower() != input[j].lower():	
			return False

		i += 1
		j -= 1	
	return True	


print is_palindrome("helle##@@##elleh")
