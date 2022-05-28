# LeetCode Problem #713: Subarray Product Less Than K

This repository contains a Python solution for the LeetCode problem #713: Subarray Product Less Than K. The function calculates the number of contiguous subarrays where the product of all the numbers in the subarray is less than `k`.

## Problem Statement

Your are given an array of positive integers `nums`. Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than `k`.

### Constraints:

- 0 < `nums.length` <= 50000.
- 0 < `nums[i]` < 1000.
- 0 <= `k` < 10^6.

## Solution Approach

The solution uses a sliding window approach. It maintains a product of all the elements in the window and adjusts the window's size by moving its left bound until the product is less than `k`. For each right bound, it counts the size of the window, which is the number of new subarrays created when a new element is added.

## Code Explanation

```python
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans, prod, i = 0, 1, 0
        for j, num in enumerate(nums):  # for each right bound
            prod *= num  # update the product
            while i <= j and prod >= k:  # adjust window size by moving left bound
                prod //= nums[i]
                i += 1
            ans += j - i + 1  # add the number of new subarrays to the answer
        return ans
```