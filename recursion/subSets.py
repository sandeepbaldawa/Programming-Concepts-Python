# From Stanford easy way to generate subsets
def getSubSets(soFar, rest):
    if len(rest) == 0:
        print soFar
        return

    getSubSets(soFar + rest[0], rest[1:]) # Either choose the character and recurse
    getSubSets(soFar, rest[1:])           # Or dont choose the character and recurse

getSubSets("","abc")
