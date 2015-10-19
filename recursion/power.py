def power(base, exp):
    if exp == 0:
        return 1
    
    half = power(base, exp/2)    
    if exp & 1: # odd number or not exp % 2
        return base * half * half
    else:
        return half * half
        
        
print power(5,3)         
print power(5,0)
print power(5,2)
print power(2,2)
