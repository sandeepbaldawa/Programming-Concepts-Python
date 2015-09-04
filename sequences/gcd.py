def gcd(a, b):
    while(b):
        a,b = b, a%b
    return a

print gcd(10,3)	
print gcd(2,4)
