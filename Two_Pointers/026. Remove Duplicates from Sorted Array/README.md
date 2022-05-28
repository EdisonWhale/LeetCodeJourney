# LeetCode Problem #26: Remove Duplicates from Sorted Array

This repository contains a Python solution for the LeetCode problem #26: Remove Duplicates from Sorted Array. The code modifies the given sorted array so that it contains only unique elements, and returns the new length.

## Problem Statement

Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.

Do not allocate extra space for another array; you must do this by modifying the input array in-place with O(1) extra memory.

### Constraints:

- 0 <= nums.length <= 3 * 10^4
- -10^4 <= nums[i] <= 10^4
- nums is sorted in ascending order.

### Test Case:

Input: `nums = [1,1,2]`

Output: `2, nums = [1,2]`

## Solution Approach

The solution uses the two-pointer technique. The 'fast' pointer moves through the array checking for changes in value, while the 'slow' pointer keeps track of the position where the next distinct element should be placed.

## Code Explanation

```
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:  
            return 0
        
        n = len(nums)
        fast = slow = 1  
        while fast < n:  
            if nums[fast] != nums[fast - 1]:  
                nums[slow] = nums[fast]  
                slow += 1  
            fast += 1  
        
        return slow  
```

Here, 'fast' and 'slow' are initialized at 1 because we are considering the difference with the previous element. The main loop traverses the array from the second element, and if the current element is different from the previous one (i.e., a change in value is detected), the current element is written to the position pointed to by the 'slow' pointer, and then the 'slow' pointer is incremented. Finally, 'slow' is returned, which represents the length of the array with distinct elements.
