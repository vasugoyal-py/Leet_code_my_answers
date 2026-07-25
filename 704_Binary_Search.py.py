class Solution:
    def search(self, nums: List[int], target: int) -> int:
        min = 0 
        max = len(nums) - 1
        n = (max + min) // 2

        while min <= max:
            if target > nums[n]:
                min = n +1
                n = (max + min) // 2
            elif target < nums[n]:
                max = n - 1
                n = (max + min) // 2
            if target == nums[n]:
                return n
        return (-1)