# LeetCode Problem #80: Remove Duplicates from Sorted Array II

This repository contains a Python solution for LeetCode problem #80: Remove Duplicates from Sorted Array II. The solution modifies the given sorted array so that duplicates appear at most twice.

## Problem Statement

Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length. Do not allocate extra space for another array; you must do this by modifying the input array in-place with O(1) extra memory.

### Constraints:

- 1 <= nums.length <= 3 * 10^4
- -10^4 <= nums[i] <= 10^4
- nums is sorted in ascending order.

### Test Case:

Input: `nums = [1,1,1,2,2,3]`

Output: `5`

## Solution Approach

The solution uses a slow and fast pointer approach. The slow pointer indicates the next position to be replaced, and the fast pointer is used to scan the entire array. If the fast pointer points to a number different from the number that the slow pointer is two positions before, the number at the fast pointer is placed at the position of the slow pointer, and then the slow pointer moves one step to the right.

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

For each element in nums, if it's different from the number that is two positions before the current slow pointer, it is placed at the position of the slow pointer, then the slow pointer moves one step forward.
