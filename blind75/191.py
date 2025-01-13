# Leetcode 191: Number of 1 Bits

# bitwise operation
def hammingWeight(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

# Brian Kernighan's Algorithm
def hammingWeightKernighan(n):
    count = 0
    while n:
        n &= n-1
        count += 1
    return count

n = 11
# print(hammingWeight(n))

# how to convert a number to binary without using inbuilt function?
# 11//2 = 5, 11%2 = 1
# 5//2 = 2, 5%2 = 1
# 2//2 = 1, 2%2 = 0
# 1//2 = 0, 1%2 = 1
# to implement the above in code:
# n = 11
# while n:
#     print(n%2)
#     n //= 2

def hamweight(n):
    number = []
    count = 0
    while n:
        number.append(n%2)
        n //= 2
        # print(number[-1])
        if number[-1] == 1:
            count += 1
            # print(count)
    # print(number)
    return count
    

def hamw8t(n):
    count = 0
    while n:
        if n % 2 == 1:  # Check if the last bit is 1
            count += 1
        n //= 2  # Shift bits by dividing by 2
    return count

print(hamw8t(7))