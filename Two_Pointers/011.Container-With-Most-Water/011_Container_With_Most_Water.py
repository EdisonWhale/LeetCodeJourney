class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1  
        ans = 0  # To hold the max area
        while l < r:  # Until the pointers meet
            area = min(height[l], height[r]) * (r - l)  # Calculate the area
            ans = max(ans, area)  # Update max area if current area is larger
            if height[l] <= height[r]:  # Move the pointer of the smaller height
                l += 1
            else:
                r -= 1
        return ans  