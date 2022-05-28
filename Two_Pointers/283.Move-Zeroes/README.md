# LeetCode Problem #283: Move Zeroes

This repository contains a Python solution for the LeetCode problem #283: Move Zeroes. The function moves all zeros in the list to the end while maintaining the relative order of the non-zero elements.

## Problem Statement

Given an array `nums`, write a function to move all `0`'s to the end of it while maintaining the relative order of the non-zero elements. 

### Constraints:

- You must do this in-place without making a copy of the array.
- Minimize the total number of operations.

## Solution Approach

The solution uses two pointers, `i` and `j`. `i` is the fast pointer and `j` is the slow pointer. The slow pointer `j` maintains the position of the next zero found in the array. The fast pointer `i` is used to find the non-zero elements. When a non-zero element is found, we swap the non-zero element with the first zero found in the array.

## Code Explanation

```python
class Solution(object):
    def moveZeroes(self, nums):
        if not nums:
            return 0
        j = 0  # j pointer keeps track of the number of non-zero elements
        for i in range(len(nums)):
            if nums[i]:  # If element is non-zero
                nums[j] = nums[i]  # Swap with the element at j
                j += 1  # Increase the non-zero count
        for i in range(j, len(nums)):  # From the first zero position to the end
            nums[i] = 0  # Set all elements to zero
```