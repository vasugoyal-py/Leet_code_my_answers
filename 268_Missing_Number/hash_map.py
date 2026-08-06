class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        dic = {}
        for y,x in enumerate(nums):
            dic[x] = y

        n = len(nums) + 1
        for num in range(n):
            if num not in dic:
                return num
