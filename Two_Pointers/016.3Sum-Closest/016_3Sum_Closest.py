class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()  # Sort the array
        n = len(nums)  # Get the length of the array
        best = 10**7  # Initialize the best solution
        
        # Update the best solution based on the absolute difference from the target
        def update(cur):
            nonlocal best
            if abs(cur - target) < abs(best - target):
                best = cur

        # Enumerate a
        for i in range(n):
            # Ensure the current number is different from the last enumerated number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # Use two pointers to enumerate b and c
            j, k = i + 1, n - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                # If the sum equals the target, return the target directly
                if s == target:
                    return target
                update(s)
                if s > target:
                    # If the sum is larger than the target, move the pointer of c
                    k0 = k - 1
                    # Move to the next different element
                    while j < k0 and nums[k0] == nums[k]:
                        k0 -= 1
                    k = k0
                else:
                    # If the sum is smaller than the target, move the pointer of b
                    j0 = j + 1
                    # Move to the next different element
                    while j0 < k and nums[j0] == nums[j]:
                        j0 += 1
                    j = j0

        return best  # Return the best solution
