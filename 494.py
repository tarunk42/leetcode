# Leetcode 494: Target Sum
# Problem Description:
# You are given an integer array nums and an integer target.
# You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.
# For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
# Return the number of different expressions that you can build, which evaluates to target.


# brute force
def findTargetSumWays(nums, target): 
    def calculate(nums, i, sum, S):                                                  # S is the target, sum is the current sum, i is the current index, nums is the array
        if i == len(nums):                                                           # if we reach the end of the array
            return 1 if sum == S else 0                                              # if the sum is equal to the target, return 1, else return 0
        return calculate(nums, i+1, sum + nums[i], S) + calculate(nums, i+1, sum - nums[i], S) # return the sum of the two recursive calls
    return calculate(nums, 0, 0, target)                                                       # return the result of the recursive function


# dynamic programming
def findTargetSumWaysDP(nums, target):
    total_sum = sum(nums)
    if total_sum < target or (total_sum + target) % 2:
        return 0
    S = (total_sum + target) // 2
    dp = [0] * (S + 1)
    dp[0] = 1
    for num in nums:
        for i in range(S, num-1, -1):
            dp[i] += dp[i-num]
    return dp[S]

nums = [1,1,1,1,1]
target = 3
print(findTargetSumWays(nums, target))