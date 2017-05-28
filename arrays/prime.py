def isPrime(num):
  if num <= 1:
    return 0

  if num > 0 and num % 2 == 0:
    return 0

  for i in range(3,num,2):
     if num % i == 0:
       return 0
  return 1  
print isPrime(4)
print isPrime(5)
~                 
