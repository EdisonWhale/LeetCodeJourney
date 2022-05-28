# LeetCode Problem #18: 4Sum

This repository contains a Python solution for the LeetCode problem #18: 4Sum. The code finds all unique quadruplets in the array which gives the sum of target.

## Problem Statement

Given an array `nums` of n integers and an integer `target`, are there elements a, b, c, and d in `nums` such that a + b + c + d = `target`? Find all unique quadruplets in the array which gives the sum of target.

### Constraints:

- The solution set must not contain duplicate quadruplets.
- `nums` length is less than or equal to 200.
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9

### Test Case:

Input: `nums = [1,0,-1,0,-2,2], target = 0`

Output: `[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]`

## Solution Approach

This solution follows a similar approach to 3sum problem but here, we are trying to find 4 numbers that add up to a target value. The time complexity of the approach is approximately O(n^3). This solution includes necessary pruning to reduce computational overhead.

In Python, we first sort the input list, which is a prerequisite for skipping duplicates and for the two-pointer technique used later. We then use three for-loops to iterate through the list, with each loop iterating one of the four numbers we are trying to find. For the fourth number, we use the two-pointer technique.

## Code Explanation

```
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        quadruplets = list()
        if not nums or len(nums) < 4:
            return quadruplets
        
        nums.sort()  # Sorting the array is essential
        length = len(nums)
        for i in range(length - 3):  # The first loop
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicate number
                continue
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:  # Pruning
                break
            if nums[i] + nums[length - 3] + nums[length - 2] + nums[length - 1] < target:  # Pruning
                continue
            for j in range(i + 1, length - 2):  # The second loop
                if j > i + 1 and nums[j] == nums[j - 1]:  # Skip duplicate number
                    continue
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:  # Pruning
                    break
                if nums[i] + nums[j] + nums[length - 2] + nums[length - 1] < target:  # Pruning
                    continue
                left, right = j + 1, length - 1  # The third and fourth numbers are determined by the two-pointer technique
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:  # Find a quadruplet
                        quadruplets.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:  # Skip the same number
                            left += 1
                        left += 1
                        while left < right and nums[right] == nums[right - 1]:  # Skip the same number
                            right -= 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        
        return quadruplets

```