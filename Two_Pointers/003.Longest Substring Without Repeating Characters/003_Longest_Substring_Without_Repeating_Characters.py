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
