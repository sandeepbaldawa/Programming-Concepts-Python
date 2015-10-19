def isPalindrome(str):
    if len(str) == 0:
        return True
    
    return str[0] == str[len(str)-1] and isPalindrome(str[1:-1])
    
print isPalindrome("day") 
print isPalindrome("dad")
print isPalindrome("m")    
print isPalindrome("lololol")
