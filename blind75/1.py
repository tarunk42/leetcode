def two_sum(nums, target):
    index_map = {}
    for i in range(len(nums)):
        sub = target - nums[i]

        if sub in index_map:
            return [i, index_map[sub]]
        
        index_map[nums[i]] = i


nums = [2, 7, 11, 15]
target = 9

# One-Pass Hash Map
print(two_sum(nums, target))    # Output: [0, 1]

