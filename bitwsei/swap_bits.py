#Below just toggles the bits when we know the bits are different..
def swap_bits(x, i, j):
    # Toggle bits only if both ith and jth value are diff
    if ((x >> i) & 1) != ((x >> j) & 1):
        bit_mask =  ((1 << i) | (1<< j))
        x = x ^ bit_mask

