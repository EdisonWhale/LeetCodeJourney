# LeetCode Problem #259: 3Sum Smaller

This repository contains a Python solution for LeetCode problem #259: 3Sum Smaller. The solution calculates the number of triplets whose sum is smaller than the given target.

## Problem Statement

Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

### Constraints:

- n == nums.length
- 0 <= n <= 3000
- -10^5 <= nums[i] <= 10^5
- -10^5 <= target <= 10^5

### Test Case:

Input: `nums = [-2,0,1,3], target = 2`

Output: `2`

## Solution Approach

The solution uses a two-pointer approach along with sorting of the array. For each element, we use a two-pointer approach to find the pairs whose sum with the current element is less than the target.

## Code Explanation

```
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        if len(nums) < 3:
            return 0
        
        res = 0 
        nums.sort() 
         
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]
                if three_sum < target:
                    res += right - left
                    left += 1
                else:
                    right -= 1
        return res
```

For each index 'i', we look for pairs in the rest of the array whose sum with 'nums[i]' is less than the target. 'left' and 'right' are the two pointers initialized at the next to 'i' and the last element of 'nums'. If the sum is less than the target, we move the left pointer to the right. If the sum is larger or equal to the target, we move the right pointer to the left.
