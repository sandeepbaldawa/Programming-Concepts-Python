'''
Given excel column in strings decode the id's in integers
eg:- A=1, B=2, C=3..AA=27 AB=28 etc..
'''

def decode_column_id(col):
   result = 0
   for each in col:
      result = result * 26 + ((ord(each) - ord('A') + 1))
   print result

def decode_column(col):
   print reduce(lambda result, c: result * 26 + ((ord(c) - ord('A') + 1)), col, 0)

decode_column("AA")
