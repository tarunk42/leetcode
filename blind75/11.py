# Leetcode 11: Container With Most Water

# brute force
def maxArea(height):
    max_area = 0
    for i in range(len(height)):
        for j in range(i+1, len(height)):
            max_area = max(max_area, min(height[i], height[j]) * (j-i))
    return max_area

# two pointer
def maxAreaTwoPointer(height):
    max_area = 0
    left, right = 0, len(height)-1
    while left < right:
        area = min(height[left], height[right]) * (right-left)
        max_area = max(max_area, area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area


height = [1,8,6,2,5,4,8,3,7]
# height = [1,1]
print(maxArea(height))
print(maxAreaTwoPointer(height))