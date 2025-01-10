# Leetcode 33. Search in Rotated Sorted Array

# Brute Force
def search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

# Binary Search
def search_binary_search(nums, target):
    n = len(nums)
    left, right = 0, n-1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] >= nums[left]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


nums = [4,5,6,7,0,1,2]
target = 0
print(search(nums, target))
print(search_binary_search(nums, target))