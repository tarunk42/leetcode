# Leetcode: 15. 3Sum

# Brute Force
def threeSum(nums):
    nums.sort()
    n = len(nums)
    result = set()
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if nums[i] + nums[j]+ nums[k] == 0:
                    result.add(tuple(sorted([nums[i], nums[j], nums[k]])))

    return list(result)


# Two Pointer Solution
def threeSum_twoPass(nums):
    nums.sort()
    result = []
    n = len(nums)

    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        target = -nums[i]
        left, right = i + 1, n-1

        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum == target:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1
    return result

def threeSum_hashmap(nums):
    nums.sort()
    n = len(nums)
    result = set()

    for i in range(n):
        target = -nums[i]
        index_map = {}
        for j in range(i+1, n):
            sub = target - nums[j]
            if sub in index_map:
                result.add((nums[i], nums[j], sub))
            index_map[nums[j]] = j
    return [list(t) for t in result]

nums = [-1,0,1,2,-1,-4]

print(threeSum(nums))
print(threeSum_twoPass(nums))
print(threeSum_hashmap(nums))