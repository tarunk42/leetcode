# Leetcode 11: Container With Most Water

def maxArea(height):
    """
    This function calculates the maximum area of water that can be trapped between lines
    in a histogram. It uses the two-pointer approach for optimal performance.
    
    Args:
        height (list): A list of integers representing the histogram's bar heights.
        
    Returns:
        int: The maximum area of water that can be trapped.
    """
    max_area = 0
    left = 0
    right = len(height) - 1
    
    while left < right:
        # Calculate the width of the current area
        width = right - left
        # The height is determined by the shorter bar
        current_height = min(height[left], height[right])
        # Calculate the current area
        current_area = current_height * width
        # Update the maximum area if current area is larger
        max_area = max(max_area, current_area)
        
        # Move the pointer pointing to the shorter bar
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
            
    return max_area

# Example usage:
height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))  # Output: 49
