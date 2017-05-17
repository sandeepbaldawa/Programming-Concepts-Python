def swap_bits(x):
    even_bits = x & 0xAAAAAAAA
    odd_bits  = x & 0x55555555
    
    even_bits >>= 1 # shit even bits to odd position
    odd_bits <<= 1  # shit odd bits to even position
    return even_bits | odd_bits
