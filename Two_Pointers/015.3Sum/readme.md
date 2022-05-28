# LeetCode Solution: 15. 3Sum

This problem, "3Sum", is a classic problem which employs the two-pointers technique. It is essential to fully understand and be able to quickly and accurately implement a solution for it.


## Key Details:
1. Sorting the array at the very start is a crucial step:
```python
   nums.sort()
```
2. To avoid duplicates, ensure to move the left and right pointers only after confirming that a solution has been found. Do not skip duplicates before checking if the solution holds:
```python
   if nums[second] + nums[third] == target:
       ans.append([nums[first], nums[second], nums[third]])
```
3. For the outermost loop, ascertain to begin the inner loop before skipping duplicates from the outer loop:
```python
   for first in range(n):
       if first > 0 and nums[first] == nums[first - 1]:
           continue
```