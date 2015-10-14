# Beautiful piece of code from Stanford classes

def getPerms(soFar, rest):
    if len(rest) == 0:
        print soFar
        return

    for i in range(0,len(rest)):
        first = soFar + rest[i]           # Choose one letter into your string to form the final permutation eg:- "a"
        second = rest[:i] + rest[i+1:]    # Leave the remaining here eg:- "bcde"
        getPerms(first, second)

getPerms("", "abcde")
