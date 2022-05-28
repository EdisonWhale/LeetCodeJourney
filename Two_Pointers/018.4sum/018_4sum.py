class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        quadruplets = list()
        if not nums or len(nums) < 4:
            return quadruplets
        
        nums.sort()  # Sorting the array is essential
        length = len(nums)
        for i in range(length - 3):  # The first loop
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicate number
                continue
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:  # Pruning
                break
            if nums[i] + nums[length - 3] + nums[length - 2] + nums[length - 1] < target:  # Pruning
                continue
            for j in range(i + 1, length - 2):  # The second loop
                if j > i + 1 and nums[j] == nums[j - 1]:  # Skip duplicate number
                    continue
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:  # Pruning
                    break
                if nums[i] + nums[j] + nums[length - 2] + nums[length - 1] < target:  # Pruning
                    continue
                left, right = j + 1, length - 1  # The third and fourth numbers are determined by the two-pointer technique
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:  # Find a quadruplet
                        quadruplets.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:  # Skip the same number
                            left += 1
                        left += 1
                        while left < right and nums[right] == nums[right - 1]:  # Skip the same number
                            right -= 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        
        return quadruplets
