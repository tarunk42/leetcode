# Leetcode 338. Counting Bits

# Brute force
def countBitsBrute(n):
    res = []
    for i in range(n+1):
        res.append(bin(i).count('1'))
    return res

# Dynamic Programming
def countBitsDP(n):
    res = [0] * (n+1)
    for i in range(1, n+1):
        # res[i] = res[i//2] + i%2
        res[i] = res[i>>1] + i&1
    return res

# Dynamic Programming (Using Most Significant Bit)
def countBitsMSB(n):
    res = [0] * (n+1)
    msb = 0
    for i in range(1, n+1):
        if i & (i-1) == 0:
            msb = i
        res[i] = res[i-msb] + 1
    return res

def countBits(n):
    def count_ones(num):
        count = 0
        while num > 0:
            count += num % 2  
            num //= 2 
        return count

    result = []
    for i in range(n + 1):
        result.append(count_ones(i))  
    return result

import time
start = time.time()
countBits(10000000)
print(time.time() - start)

start = time.time()
countBitsDP(10000000)
print(time.time() - start)

start = time.time()
countBitsMSB(10000000)
print(time.time() - start)

start = time.time()
countBitsBrute(10000000)
print(time.time() - start)

# what is meant by i>>1 and i&1?
# i >> 1 is equivalent to i // 2
# i & 1 is equivalent to i % 2
# For example, 5 >> 1 is 2 and 5 & 1 is 1
# 5 in binary is 101, 2 in binary is 10, and 1 in binary
# does this >> operator automatically convert the number to binary?
# No, the >> operator does not convert the number to binary. 
# The >> operator is a bitwise right shift operator that shifts the bits of the number to the right by the specified number of positions. 
# For example, 5 >> 1 shifts the bits of the binary representation of 5 (101) to the right by 1 position, resulting in 2 (10).
# Is there any left shift operator?
# Yes, there is a left shift operator << that shifts the bits of the number to the left by the specified number of positions.
# what is it equivalent to?
# The left shift operator << is equivalent to multiplying the number by 2 to the power of the specified number of positions.
# For example, 5 << 1 is equivalent to 5 * 2^1, which is 10.
# what is it used for?
# The left shift operator << is commonly used in bitwise operations to efficiently multiply or divide a number by powers of 2.
# For example, shifting a number to the left by 1 position is equivalent to multiplying it by 2, and shifting it to the right by 1 position is equivalent to dividing it by 2.