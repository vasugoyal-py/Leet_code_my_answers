class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        duplicates = 0

        for j in range(1, len(nums)):
            if nums[duplicates] != nums[j]:
                duplicates += 1
                nums[duplicates] = nums[j]
        return duplicates + 1