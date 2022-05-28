# 75: Sort Colors

This repository contains a Python solution for LeetCode problem #75: Sort Colors. The solution categorizes and sorts colors represented by 0, 1, and 2, in the given array in-place.

## Problem Statement

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue. We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

### Constraints:

- n == nums.length
- 1 <= n <= 300
- nums[i] is 0, 1, or 2.

### Test Case:

Input: `nums = [2,0,2,1,1,0]`

Output: `None` (The sorted array in-place: `[0,0,1,1,2,2]`)

## Solution Approach

The solution uses two-pass approach. First pass to sort zeros, and second pass to sort ones. Two pointers are used, one to traverse the array and another to keep track of the position where the next 0 or 1 should be placed.

## Code Explanation

```
class Solution(object):
    def removeDuplicates(self, nums):
        slow = 0
        for fast in range(len(nums)):
            if slow < 2 or nums[fast] != nums[slow - 2]:
                nums[slow] = nums[fast]
                slow += 1
        return slow
```

The pointer `ptr` is initially at position 0. The first loop goes through the array, whenever it finds a `0`, it swaps this 0 with the number at `ptr` position and moves `ptr` one step forward. This ensures all `0`s are at the beginning of the array. In the second loop, it starts from the `ptr` position to the end of the array, whenever it finds a `1`, it swaps this `1` with the number at `ptr` position and moves `ptr` one step forward. Thus, all `1`s follow the `0`s. The remaining numbers will be `2`s, which are already in their correct position.