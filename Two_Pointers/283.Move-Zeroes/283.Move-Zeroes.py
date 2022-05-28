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