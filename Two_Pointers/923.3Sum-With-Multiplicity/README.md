# LeetCode Problem #923: 3Sum With Multiplicity

This repository contains a Python solution for the LeetCode problem #923: 3Sum With Multiplicity. The function calculates the number of tuples (i, j, k) such that they form a sum equal to `target`, and i < j < k.

## Problem Statement

Given an integer array A, and an integer `target`, return the number of tuples i, j, k such that i < j < k and A[i] + A[j] + A[k] == `target`. As the answer can be very large, return it modulo 10^9 + 7.

### Constraints:

- 3 <= A.length <= 3000
- 0 <= A[i] <= 100
- 0 <= target <= 300

## Solution Approach

This solution uses a 3Sum approach with Counter and a sorted keys list for optimization. For every number `x`, we calculate `T = target - x`, and then we try to find two other numbers `y` and `z` from the sorted keys list that sum up to `T`. To avoid duplicate tuples, we make sure `i <= j <= k`. We then add the count of these tuples to the answer.

## Code Explanation

```python
class Solution(object):
    def threeSumMulti(self, A, target):
        MOD = 10**9 + 7
        count = collections.Counter(A)
        keys = sorted(count)

        ans = 0

        for i, x in enumerate(keys):
            T = target - x
            j, k = i, len(keys) - 1
            while j <= k:
                y, z = keys[j], keys[k]
                if y + z < T:
                    j += 1
                elif y + z > T:
                    k -= 1
                else: # x+y+z == T, now calculate the size of the contribution
                    if i < j < k:
                        ans += count[x] * count[y] * count[z]
                    elif i == j < k:
                        ans += count[x] * (count[x] - 1) / 2 * count[z]
                    elif i < j == k:
                        ans += count[x] * count[y] * (count[y] - 1) / 2
                    else:  # i == j == k
                        ans += count[x] * (count[x] - 1) * (count[x] - 2) / 6

                    j += 1
                    k -= 1

        return ans % MOD
```