def x_pow_y(x, y):
    res = 1.0
    power = y
    while (power):
        if power & 1:
            res*= x
        x *= x
        power >>= 1
    print res

x_pow_y(2,7)
x_pow_y(2,10)
"""
y=10 res=1 x=4  => even
y=5 res=4 x=16  => odd
y=2 res=4 x=256 => even
y=1 res=4*256 x=256*256  => odd
"""
