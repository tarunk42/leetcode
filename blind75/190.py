# Leetcode 190. Reverse Bits

# Reverse bits of a given 32 bits unsigned integer.

# brute force (bit manipulation)
def reverseBits(n: int) -> int:
    res = 0
    for i in range(32):
        res = (res << 1) + (n & 1)
        n >>= 1
    return res

# example
n = 43261596
print(reverseBits(n)) # 964176192
