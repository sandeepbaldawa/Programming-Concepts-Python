# x & ~(x-1) => Isolates the right most "1"

# return 1 for odd no of 1's and 0 otherwise
def parity(x):
   count = 0
   while(x):
      rightmost_one = x & ~(x - 1)
      x = x ^ rightmost_one # Removes rightmost one
      count += 1
   return count % 2   
   
# Count number of 1's   
def count_bits(x):
   count = 0
   while(x):
      rightmost_one = x & ~(x - 1)
      x = x ^ rightmost_one # Removes rightmost one
      count += 1
   return count   
