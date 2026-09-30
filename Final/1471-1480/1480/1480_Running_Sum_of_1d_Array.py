class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        new_lis = []
        total  = 0
        for i in nums:
            total  += i
            new_lis.append(total)
        return new_lis