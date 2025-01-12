# Leetcode 268. Missing Number

# Brute Force
def missingNumber(nums):
    n = len(nums)
    nums.sort()
    for i in range(n):
        if nums[i] != i:
            return i
    return n

# Bit Manipulation
def missingNumber_bit_manipulation(nums):
    missing = len(nums)
    for i, num in enumerate(nums):
        missing ^= i ^ num

    return missing

# Gauss' Formula

def missingNumber_gauss(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum





nums = [0,1]
print(missingNumber(nums))