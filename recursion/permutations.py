# Beautiful piece of code from Stanford classes
# N! permutations

def getPerms(soFar, rest):
    if len(rest) == 0:
        print soFar
        return

    for i in range(0,len(rest)):
        first = soFar + rest[i]           # Choose one letter into your string to form the final permutation eg:- "a"
        second = rest[:i] + rest[i+1:]    # Leave the remaining here eg:- "bcde"
        getPerms(first, second)

getPerms("", "abcde")


# Second method, does not create new array each time and passes indices..

def printPerm(arr):
   n = len(arr) - 1
   helper(arr, 0, n)

def helper(arr, soFar_idx, n):
   if soFar_idx == n:
      print(arr)
      return

   for i in range(len(arr)):
     arr[i], arr[soFar_idx] = arr[soFar_idx], arr[i] # swap
     helper(arr, soFar_idx + 1, n)
     arr[soFar_idx], arr[i] = arr[i], arr[soFar_idx] # reset swap

printPerm(['a','b','c','d'])
