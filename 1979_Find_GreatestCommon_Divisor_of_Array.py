class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        def gcd(x, y):
            while y != 0:
                x, y = y, x % y
            return x
        return gcd(nums[0], nums[-1])