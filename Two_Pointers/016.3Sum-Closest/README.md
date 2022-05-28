# LeetCode Solution: 16. 3Sum Closest

This problem, "3Sum Closest", is another classic problem involving the two-pointers technique. It is important to fully understand and be able to quickly and accurately implement a solution for it.

## Problem Description

Given an array `nums` of n integers and an integer `target`, find three integers in `nums` such that the sum is closest to `target`. Return the sum of the three integers. You may assume that each input would have exactly one solution.

## Example

Input: nums = [-1,2,1,-4], target = 1<br/>
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

## Key Details:
1. Sorting the array at the very start is a crucial step:
```python
   nums.sort()
```
2. An update function is used to update the best solution based on the absolute difference from the target.

3.  For each 'a' enumerated in the array, a pair of pointers 'b' and 'c' is used to find the solution. If the sum of the three numbers equals the target, return the target as the result directly. Otherwise, update the best solution and adjust 'b' and 'c' accordingly.

4. The iteration is optimized by skipping over the duplicate elements.