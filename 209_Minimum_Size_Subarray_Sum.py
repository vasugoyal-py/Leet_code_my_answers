class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0 
        n = len(nums)
        best = float('inf')
        current = 0

        for r in range(n):
            current += nums[r]
            while current >= target:
                best = min(best, r - l + 1)
                current -= nums[l]
                l += 1
                
        if best == float('inf'):
            return 0
        else:
            return best