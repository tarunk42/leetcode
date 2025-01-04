# Leetcode 153. Find Minimum in Rotated Sorted Array

# Brute Force
def findMin(nums):
    n = len(nums)
    if n == 1:
        return nums[0]
    for i in range(1, n):
        if nums[i] < nums[i-1]:
            return nums[i]
    return nums[0]

# Binary Search
def findMin_binary_search(nums):
    n = len(nums)
    left, right = 0, n-1
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]

nums = [3,4,5,1,2]
print(findMin(nums))
print(findMin_binary_search(nums))