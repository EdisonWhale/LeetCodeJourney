class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        def quadratic(x):
            return a*x*x + b*x + c 
        n = len(nums)
        index = 0 if a < 0 else n-1  # index position based on sign of 'a'
        l, r, ans = 0, n-1, [0] * n
        while l <= r:
            l_val, r_val = quadratic(nums[l]), quadratic(nums[r])  # compute quadratic for l and r
            if a >= 0:  # for positive 'a'
                if l_val > r_val:  # choose larger value
                    ans[index] = l_val 
                    l += 1
                else:    
                    ans[index] = r_val 
                    r -= 1
                index -= 1  # move index towards center
            else:  # for negative 'a'
                if l_val > r_val:  # choose smaller value
                    ans[index] = r_val 
                    r -= 1
                else:    
                    ans[index] = l_val 
                    l += 1
                index += 1  # move index towards center
        return ans