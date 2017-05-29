'''
You are given an array of characters arr that consists of sequences of characters separated by space characters. 
Each space-delimited sequence of characters defines a word.

Implement a function reverseWords that reverses the order of the words in the array in the most efficient manner.

Explain your solution and analyze its time and space complexities.

Example:

input:  arr = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', '  ',
                'm', 'a', 'k', 'e', 's', '  ',
                'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]

output: [ 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e', '  ',
          'm', 'a', 'k', 'e', 's', '  ',
          'p', 'e', 'r', 'f', 'e', 'c', 't' ]
          
'''

def reverse(arr, start, end):
   while(start < end):
     print start, end
     arr[start], arr[end] = arr[end], arr[start]
     start += 1
     end -= 1
   return arr

def reverseWords(arr):
  ''' Reverse words order maintaining the letter order within each word
      args: arr
      return: reversed word order

      DS:
      Use array in place
      
      Time:- O(N)
      Space:- O(1)

      Algo:
      1. Reverse all letters in arr
      2. Reverse each letter in each word
  '''
  # Reverse all letters in arr
  reverse(arr, 0, len(arr)-1)

  # Reverse each word's letters
  start_word = 0
  for i in range(len(arr)):
    if arr[i] == '  ':
      reverse(arr, start_word, i-1)
      start_word = i+1
    if i == len(arr) - 1:
      reverse(arr, start_word, i)
  return arr

arr = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', '  ',
                'm', 'a', 'k', 'e', 's', '  ',
                'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]
print reverseWords(arr)
