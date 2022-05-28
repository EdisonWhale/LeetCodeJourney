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