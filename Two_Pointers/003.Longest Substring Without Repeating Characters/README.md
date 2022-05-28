# LeetCode Problem #3: Longest Substring Without Repeating Characters

Given a string `s`, find the length of the longest substring without repeating characters.

## Problem Statement

Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

### Constraints:

- Input: s = "abcabcbb"
- Output: 3
- Explanation: The answer is "abc", with the length of 3.

### Test Case:

Input: `nums = [-2,0,1,3], target = 2`

Output: `2`

## Solution Approach

The solution uses a two-pointer approach along with sorting of the array. For each element, we use a two-pointer approach to find the pairs whose sum with the current element is less than the target.

## Code Explanation

```
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        # Store seen characters and their positions
        seen = {}
        # Start of the window
        l = 0
        # Maximum length of substring without repeating characters
        length = 0
        for r in range(len(s)):
            char = s[r]
            # If character is seen and is within current window
            if char in seen and seen[char] >= l:
                # Move the start of the window
                l = seen[char] + 1
            else:
                # Update the maximum length
                length = max(length, r - l + 1)
            # Update the last seen position of the character
            seen[char] = r
        return length


```

In this solution, we use a sliding window approach. We maintain a window of characters with no repeating elements. When we encounter a character that is already in the window, we move the start of the window to the right of the repeating character's previous occurrence. At each step, we update the maximum length of the window we have seen so far.