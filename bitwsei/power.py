# x ^ y normally is x multiplies y no of times O(2^N)
# Bitwise can make this just O(N)
# where N is no of bits

def power(x,y):
   res, pow = 1.0, y
   if pow < 0:
      x, y = 1/x, -y
      
   while(pow):
      if x & 1: # odd no
         res *= x
      x, pow = x * x, pow >> 1
   return res   
   
   
