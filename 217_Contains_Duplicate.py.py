class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for j,i in enumerate(nums):
            if i not in dic:
                dic[i] = j
            else:
                return True
        return False