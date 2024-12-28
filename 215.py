# 217. Contains Duplicate

# HashSet Solution
def containsFuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

# Brute Force Solution
def containDuplicateBruteForce(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i+i, n):
            if nums[i] == nums[j]:
                return True
    return False

nums = [1,2,3,1]
import time
start = time.time()
print(containsFuplicate(nums))
print(time.time() - start)  

start = time.time()
print(containDuplicateBruteForce(nums))
print(time.time() - start)