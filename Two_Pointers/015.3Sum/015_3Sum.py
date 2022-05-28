class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = list()

        for first in range(n):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            # Initialize the third pointer to the rightmost side of the array
            third = n - 1
            # Set target as the negative of the first number
            target = -nums[first]

            for second in range(first + 1, n):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                while second < third and nums[second] + nums[third] > target:
                    third -= 1
                if second == third:
                    break
                # If the sum of the numbers at the b and c pointers equal to the target, append the solution to the answer list
                if nums[second] + nums[third] == target:
                    ans.append([nums[first], nums[second], nums[third]])
        
        return ans
