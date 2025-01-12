# Leetcode 371: Sum of Two Integers
# Not Done Yet

# bitwise operation
def getSum(a, b):
    mask = 0xffffffff
    while b & mask:
        a, b = a ^ b, (a & b) << 1
    return a & mask if b > mask else a

# recursive
def getSumRecursion(a, b):
    return a if b == 0 else getSum(a^b, (a&b)<<1)

a = 1
b = 2
print(getSum(a, b))
print(getSumRecursion(a, b))