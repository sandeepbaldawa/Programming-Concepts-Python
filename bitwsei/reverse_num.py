def reverse(x):
   res , last_digit = 0, 0
   while(x):
     last_digit = x % 10
     res = res * 10 + last_digit
     x = x/10

   return res
print reverse(321)
