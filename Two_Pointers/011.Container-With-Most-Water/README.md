# LeetCode Problem #11: Container With Most Water

This repository contains a Python solution for LeetCode problem #11: Container With Most Water. The solution calculates the maximum area that can be formed between the vertical lines using the height array.

## Problem Statement

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which together with the x-axis forms a container, such that the container contains the most water.

### Constraints:

- n == height.length
- 2 <= n <= 10^5
- 0 <= height[i] <= 10^4

### Test Case:

Input: `height = [1,8,6,2,5,4,8,3,7]`

Output: `49`

## Solution Approach

The solution uses the two-pointer approach to calculate the area between two lines and iteratively updates the maximum area.

## Code Explanation

@@@
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        ans = 0
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            ans = max(ans, area)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return ans
@@@

In the code, 'l' and 'r' are the left and right pointers respectively. We calculate the area formed between the lines pointed by 'l' and 'r' and update our answer 'ans' with the maximum of the current area and previous 'ans'. We increment 'l' when the height at 'l' is less than or equal to the height at 'r', else we decrement 'r'. This way, we are always moving towards the higher height line.
