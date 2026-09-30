class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closet = nums[0]

        for x in nums:
            if abs(x) < abs(closet):
                closet = x
            elif abs(x) == abs(closet):
                closet = max(x, closet)
        return closet