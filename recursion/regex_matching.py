# http://articles.leetcode.com/2011/09/regular-expression-matching.html
# If there is a "+" compare first character(d0es not match return Fale) and then replace with * and continue same logic"
def match(string, pattern):
    if len(pattern) == 0 and len(string) == 0:
        return True

    if (len(pattern) == 0 and len(string) > 0) or (len(pattern) > 0 and len(string) == 0):
        return False

    if pattern[0] == "*":
        return match(string[1:], pattern[1:]) or match(string[1:], pattern)
    elif (pattern[0] == string[0]) or ((pattern[0] == ".") and string[0]):
        return match(string[1:], pattern[1:])
    else:
        return False

print match("abracadabra", "ab*ca*br*")
print match("abbb", "a.*b")
print match("abbb", "a.*bc")
print match("a","")
print match("","a")
print match("","")
