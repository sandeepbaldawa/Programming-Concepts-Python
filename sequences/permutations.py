# https://www.youtube.com/watch?v=Jf0WYAbPDKI
def permutations(word):
    if len(word) == 1:
    	return word
    perms=permutations(word[1:])
    first = word[0]
    result = []
    for perm in perms:
    	for i in range(len(perm)+1):
    		result.append(perm[:i] + first + perm[i:])
    return result       

print permutations("abc")
