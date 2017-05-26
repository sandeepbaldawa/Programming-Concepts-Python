# x & ~(x-1) => Isolates the right most "1"
# O(K) K is no of bits set to "1"
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

# For large nos like 64 bits we can use lookups
# MASK_SIZE = 16
# BIT_MASK = 0xFFFF

# x & BIT_MASK => Last 16 bits
# x >> MASK_SIZE  & BIT_MASK=> Last 16 bits removed AND NEXT 16 BITS COMEUP
# X >> MASK_SIZE * 2 & BIT_MASK
#AND SO ON..

def parity_LARGE_64BIT(x):
   BIT_MASK = 0xFFFF
   MASK_SIZE = 16
   return lookup[x & BIT_MASK] ^
          lookup[x >> MASK_SIZE & BIT_MASK] ^
          lookup[x >> 2 * MASK_SIZE & BIT_MASK] ^
          lookup[x >> 3 * MASK_SIZE & BIT_MASK] 
         
         
           

