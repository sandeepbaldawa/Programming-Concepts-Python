Cryptarithm Overview
The general idea of a cryptarithm is to assign integers to letters.
         For example, SEND + MORE = MONEY is “9567 + 1085 = 10652”
        
Q. How to attack this problem?
         -Need list of unique letters
         -Try all possible assignments of single digits
         -Different arrangement would produce a different answer
 
So, we want a permutation of the number of unique letters with unique numbers. First we need to get an expression…
 
def cryptarithm(expr):
We need to have a function that takes in a word and replaces the letters with digits, so it gives 3 5 6 4 instead of SEND. We can define this now inside cryptarithm and call it later.
    def makeCryptValue(word, map):
        # MakeCryptValue("SEND", {"S":5, "E":2, "N":1, "D":8 }) returns 5218
        result = 0
        for letter in word: #Walk through the result, get the digit and shift
            result = 10*result + map[letter] #10*result is the shift, map[letter] is the digit value
        return result
    # 1) Make list of words, so word[0] + word[1] = word[2]. Assume that the expression is well-formed.
    # Words = ["SEND", "MORE", "MONEY"]
    words = expr.replace("+"," ").replace("="," ").split(" ") #use str.split()
    # 2) Want a list of unique letters. Use sets for uniqueness
    letters = sorted(set("".join(words))) #Returns unique letters
    for digitAssignment in permutations(range(10), len(letters)): #Try every permutation of digits against letters
        #If 4 letters, groups of 4. If more than 10 letters, change the base
        map = dict(zip(letters, digitAssignment)) #Create tuples of letter/digit and put into a dictionary
        values = [makeCryptValue(word, map) for word in words] #Now call the function that we created earlier
        if (0 in [map[word[0]] for word in words]):
            #The first number of any word cannot be a leading 0! We can create a map to check this
            continue
        if (values[0] + values[1] == values[2]): #We win!
            return "%d+%d=%d" % (values[0], values[1], values[2])
    return None
