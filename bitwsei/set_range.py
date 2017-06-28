'''Write a function that takes two numbers x and y and for a bit range n and m  if a bit is set in x also set the same bit in y
Dont change bits in y which arent set in x or arent between n-m bits
f(x, y, m, n) : f(0b01010101, 0b00001111, 2, 5) =>  0b000111111
'''
# m > n
# 0b01010101 => x
# 0b00001111  => y
# bit_mask 1 << m - n + 1
# Set all bits from n to m bit_mask - 1
# Shift bit_mask by << n
# y | bit_mask
def set_range(x, y, n, m):
    bit_mask = (1 << (m - n + 1)) - 1 << n
    bits_extracted = x & bit_mask
    y = y | bits_extracted
    return bin(y)


print set_range(0b01010101, 0b00001111, 2, 5)



