class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        best = float('-inf')
        if n <= 1:
            return nums[0]

        l = 0
        sum = 0
        for r in range(n):
            if (r-l) == k:
                sum -= nums[l]
                l += 1
            
            sum += nums[r]
            if (r-l + 1) == k:
                divided = sum / k
                best = max(best,divided)
        
        return best
            
